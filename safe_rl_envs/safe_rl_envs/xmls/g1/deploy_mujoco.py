import time
import os
import mujoco.viewer
import mujoco
import numpy as np
import torch
import yaml
from safe_rl_envs import GUARD_ENV_ROOT

def get_gravity_orientation(quaternion):
    qw = quaternion[0]
    qx = quaternion[1]
    qy = quaternion[2]
    qz = quaternion[3]

    gravity_orientation = np.zeros(3)

    gravity_orientation[0] = 2 * (-qz * qx + qw * qy)
    gravity_orientation[1] = -2 * (qz * qy + qw * qx)
    gravity_orientation[2] = 1 - 2 * (qw * qw + qz * qz)

    return gravity_orientation


def pd_control(target_q, q, kp, target_dq, dq, kd):
    """Calculates torques from position commands"""
    return (target_q - q) * kp + (target_dq - dq) * kd

class G1Controller():
    def __init__(self):
        print(GUARD_ENV_ROOT)
        config_file = os.path.join(GUARD_ENV_ROOT, "safe_rl_envs/xmls/g1/configs/g1.yaml")
        with open(config_file, "r") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
            self.policy_path = os.path.join(GUARD_ENV_ROOT, "safe_rl_envs/xmls/g1/motion.pt")
            
            self.xml_path = os.path.join(GUARD_ENV_ROOT, "safe_rl_envs/output_model.xml")

            self.simulation_duration = self.config["simulation_duration"]
            self.simulation_dt = self.config["simulation_dt"]
            self.control_decimation = self.config["control_decimation"]

            self.kps = np.array(self.config["kps"], dtype=np.float32)
            self.kds = np.array(self.config["kds"], dtype=np.float32)

            self.default_angles = np.array(self.config["default_angles"], dtype=np.float32)

            self.ang_vel_scale = self.config["ang_vel_scale"]
            self.dof_pos_scale = self.config["dof_pos_scale"]
            self.dof_vel_scale = self.config["dof_vel_scale"]
            self.action_scale = self.config["action_scale"]
            self.cmd_scale = np.array(self.config["cmd_scale"], dtype=np.float32)

            self.num_actions = self.config["num_actions"]
            self.num_obs = self.config["num_obs"]
            
            self.cmd = np.array(self.config["cmd_init"], dtype=np.float32)

        # define context variables
        self.action = np.zeros(self.num_actions, dtype=np.float32)
        self.target_dof_pos = self.default_angles.copy()
        self.obs = np.zeros(self.num_obs, dtype=np.float32)

        self.counter = 0

        # Load robot model
        self.m = mujoco.MjModel.from_xml_path(self.xml_path)
        self.d = mujoco.MjData(self.m)
        self.m.opt.timestep = self.simulation_dt

        # load policy
        self.policy = torch.jit.load(self.policy_path)

    def step(self, d, action):
        
        tau = pd_control(self.target_dof_pos, d.qpos[7:], self.kps, np.zeros_like(self.kds), d.qvel[6:], self.kds)
        # d.ctrl[:] = tau
        # action = tau
        self.counter += 1
        if self.counter % self.control_decimation == 0:
            self.cmd = action
            # Apply control signal here.

            # create observation
            qj = d.qpos[7:]
            dqj = d.qvel[6:]
            quat = d.qpos[3:7]
            omega = d.qvel[3:6]

            qj = (qj - self.default_angles) * self.dof_pos_scale
            dqj = dqj * self.dof_vel_scale
            gravity_orientation = get_gravity_orientation(quat)
            omega = omega * self.ang_vel_scale

            period = 0.8
            count = self.counter * self.simulation_dt
            phase = count % period / period
            sin_phase = np.sin(2 * np.pi * phase)
            cos_phase = np.cos(2 * np.pi * phase)

            self.obs[:3] = omega
            self.obs[3:6] = gravity_orientation
            self.obs[6:9] = self.cmd * self.cmd_scale
            self.obs[9 : 9 + self.num_actions] = qj
            self.obs[9 + self.num_actions : 9 + 2 * self.num_actions] = dqj
            self.obs[9 + 2 * self.num_actions : 9 + 3 * self.num_actions] = self.action
            self.obs[9 + 3 * self.num_actions : 9 + 3 * self.num_actions + 2] = np.array([sin_phase, cos_phase])
            obs_tensor = torch.from_numpy(self.obs).unsqueeze(0)
            # policy inference
            self.action = self.policy(obs_tensor).detach().numpy().squeeze()
            # transform action to target_dof_pos
            self.target_dof_pos = self.action * self.action_scale + self.default_angles
            
        return tau

if __name__ == "__main__":
    # get config file name from command line
    # import argparse

    # parser = argparse.ArgumentParser()
    # parser.add_argument("config_file", type=str, help="config file name in the config folder")
    # args = parser.parse_args()
    # config_file = args.config_file
    # with open(f"{LEGGED_GYM_ROOT_DIR}/deploy/deploy_mujoco/configs/{config_file}", "r") as f:
    #     config = yaml.load(f, Loader=yaml.FullLoader)
    #     policy_path = config["policy_path"].replace("{LEGGED_GYM_ROOT_DIR}", LEGGED_GYM_ROOT_DIR)
    #     xml_path = config["xml_path"].replace("{LEGGED_GYM_ROOT_DIR}", LEGGED_GYM_ROOT_DIR)

    #     simulation_duration = config["simulation_duration"]
    #     simulation_dt = config["simulation_dt"]
    #     control_decimation = config["control_decimation"]

    #     kps = np.array(config["kps"], dtype=np.float32)
    #     kds = np.array(config["kds"], dtype=np.float32)

    #     default_angles = np.array(config["default_angles"], dtype=np.float32)

    #     ang_vel_scale = config["ang_vel_scale"]
    #     dof_pos_scale = config["dof_pos_scale"]
    #     dof_vel_scale = config["dof_vel_scale"]
    #     action_scale = config["action_scale"]
    #     cmd_scale = np.array(config["cmd_scale"], dtype=np.float32)

    #     num_actions = config["num_actions"]
    #     num_obs = config["num_obs"]
        
    #     cmd = np.array(config["cmd_init"], dtype=np.float32)

    # # define context variables
    # action = np.zeros(num_actions, dtype=np.float32)
    # target_dof_pos = default_angles.copy()
    # obs = np.zeros(num_obs, dtype=np.float32)

    # counter = 0

    # # Load robot model
    # m = mujoco.MjModel.from_xml_path(xml_path)
    # d = mujoco.MjData(m)
    # m.opt.timestep = simulation_dt

    # # load policy
    # policy = torch.jit.load(policy_path)

    g1_controller = G1Controller()
    target_dof_pos = g1_controller.target_dof_pos
    with mujoco.viewer.launch_passive(g1_controller.m, g1_controller.d) as viewer:
        # Close the viewer automatically after simulation_duration wall-seconds.
        start = time.time()
        while viewer.is_running() and time.time() - start < g1_controller.simulation_duration:
            
            step_start = time.time()
            tau = g1_controller.step(g1_controller.d)
            # mj_step can be replaced with code that also evaluates
            # a policy and applies a control signal before stepping the physics.
            g1_controller.d.ctrl[:] = tau
            mujoco.mj_step(g1_controller.m, g1_controller.d)
            # tau = pd_control(target_dof_pos, d.qpos[7:], kps, np.zeros_like(kds), d.qvel[6:], kds)
            # d.ctrl[:] = tau
            # # mj_step can be replaced with code that also evaluates
            # # a policy and applies a control signal before stepping the physics.
            # mujoco.mj_step(m, d)

            # counter += 1
            # if counter % control_decimation == 0:
            #     # Apply control signal here.

            #     # create observation
            #     qj = d.qpos[7:]
            #     dqj = d.qvel[6:]
            #     quat = d.qpos[3:7]
            #     omega = d.qvel[3:6]

            #     qj = (qj - default_angles) * dof_pos_scale
            #     dqj = dqj * dof_vel_scale
            #     gravity_orientation = get_gravity_orientation(quat)
            #     omega = omega * ang_vel_scale

            #     period = 0.8
            #     count = counter * simulation_dt
            #     phase = count % period / period
            #     sin_phase = np.sin(2 * np.pi * phase)
            #     cos_phase = np.cos(2 * np.pi * phase)

            #     obs[:3] = omega
            #     obs[3:6] = gravity_orientation
            #     obs[6:9] = cmd * cmd_scale
            #     obs[9 : 9 + num_actions] = qj
            #     obs[9 + num_actions : 9 + 2 * num_actions] = dqj
            #     obs[9 + 2 * num_actions : 9 + 3 * num_actions] = action
            #     obs[9 + 3 * num_actions : 9 + 3 * num_actions + 2] = np.array([sin_phase, cos_phase])
            #     obs_tensor = torch.from_numpy(obs).unsqueeze(0)
            #     # policy inference
            #     action = policy(obs_tensor).detach().numpy().squeeze()
            #     # transform action to target_dof_pos
            #     target_dof_pos = action * action_scale + default_angles

            # Pick up changes to the physics state, apply perturbations, update options from GUI.
            viewer.sync()

            # Rudimentary time keeping, will drift relative to wall clock.
            time_until_next_step = g1_controller.m.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)
