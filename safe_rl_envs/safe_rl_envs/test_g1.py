#!/usr/bin/env python

import argparse
import gym
import numpy as np  # noqa
from safe_rl_envs.envs.engine import Engine
from getkey import getkey, keys
from safe_rl_envs import G1Controller
import mujoco
import time
def run_random():

    config = {
            # robot setting
            'robot_base': 'xmls/g1_29dof_lock_upper_body.xml',  

            # task setting
            'task': 'goal',
            'goal_size': 0.5,

            # observation setting
            'observe_goal_comp': True,  # Observe the goal with a lidar sensor
            'observe_hazards': True,  # Observe the vector from agent to hazards
            
            # constraint setting
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            # lidar setting
            'lidar_num_bins': 16,
            
            # object setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'frameskip_binom_n': 1.0,
        }
    env = Engine(config)
    _ = env.reset()
    cnt = 0
    action = np.zeros(3)
    while True:
        step_start = time.time()
        
        cnt = cnt + 1
        if cnt % 100 == 0:
            action = np.random.uniform(-1, 1, 3)
        obs, reward, done, info = env.step(action)
        

        if done:
            # import ipdb;ipdb.set_trace()
            o = env.reset()
        #     # import ipdb;ipdb.set_trace()
        
        time_until_next_step = env.model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)

        env.render()

    # g1_controller = G1Controller()
    # env.model.opt.timestep = g1_controller.m.opt.timestep
    # viewer = mujoco.viewer.launch_passive(env.model, env.data)
    # # with mujoco.viewer.launch_passive(env.model, env.data) as viewer:
    #     # Close the viewer automatically after simulation_duration wall-seconds.
    #     # start = time.time()
    # while True:
        
    #     # step_start = time.time()
    #     # env.data.ctrl[:] = env.g1_controller.step(env.data)
    #     # mujoco.mj_step(env.model, env.data)
    #     env.step(np.zeros(12))
    #     # print(action)
    #     # viewer.sync()
    #     env.render_test()
            # Rudimentary time keeping, will drift relative to wall clock.
            # time_until_next_step = env.model.opt.timestep - (time.time() - step_start)
            # if time_until_next_step > 0:
            #     time.sleep(time_until_next_step)

                
    # g1_controller = G1Controller()

    # with mujoco.viewer.launch_passive(g1_controller.m, g1_controller.d) as viewer:
    #     # Close the viewer automatically after simulation_duration wall-seconds.
    #     start = time.time()
    #     while viewer.is_running() and time.time() - start < g1_controller.simulation_duration:
            
    #         step_start = time.time()
    #         action = g1_controller.step(g1_controller.d)
    #         # mj_step can be replaced with code that also evaluates
    #         # a policy and applies a control signal before stepping the physics.
    #         g1_controller.d.ctrl[:] = action
    #         mujoco.mj_step(g1_controller.m, g1_controller.d)

    #         # Pick up changes to the physics state, apply perturbations, update options from GUI.
    #         viewer.sync()

    #         # Rudimentary time keeping, will drift relative to wall clock.
    #         time_until_next_step = env.model.opt.timestep - (time.time() - step_start)
    #         if time_until_next_step > 0:
    #             time.sleep(time_until_next_step)




if __name__ == '__main__':
    run_random()

