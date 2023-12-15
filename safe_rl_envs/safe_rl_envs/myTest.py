#!/usr/bin/env python

import argparse
import gym
import safe_rl_envs  # noqa
import numpy as np  # noqa
from safe_rl_envs.envs.engine import Engine
from getkey import getkey, keys
def run_random(env_name):
    # env = gym.make(env_name)

    # config = {
    #         # robot setting
    #         'robot_base': 'xmls/fanuc_lr_mate/arm_lrmate_3.xml', 
    #         # 'robot_base': 'xmls/arm_3.xml', 
    #         'robot_locations':[(0.0,0.0)],
    #         'robot_keepout': 0.2, 
    #         'arm_range': 0.8,

    #         # task setting
    #         'task': 'goal',
    #         'goal_3D': True,
    #         'goal_z_range': [0.1,0.6],
    #         'goal_size': 0.2,
    #         'goal_keepout': 0.2,
    #         # 'goal_placements': [(-1.5, -1.5, 1.5, 1.5)],
    #         'reward_distance': 10.0,
    #         'reward_goal': 10.0,
            
    #         # observation setting
    #         'observe_goal_comp': True,  # Observe the goal with a lidar sensor
    #         'observe_hazard3Ds': False,  # Observe the vector from agent to hazards
    #         'compass_shape': 3,
    #         'sensors_obs':[],
    #         # 'sensors_obs': ['accelerometer_link_1', 'velocimeter_link_1', 'gyro_link_1', 'magnetometer_link_1',
    #         #                 'accelerometer_link_2', 'velocimeter_link_2', 'gyro_link_2', 'magnetometer_link_2',
    #         #                 'accelerometer_link_3', 'velocimeter_link_3', 'gyro_link_3', 'magnetometer_link_3',
    #         #                 'accelerometer_link_4', 'velocimeter_link_4', 'gyro_link_4', 'magnetometer_link_4',
    #         #                 'accelerometer_link_5', 'velocimeter_link_5', 'gyro_link_5', 'magnetometer_link_5',
    #         #                 'touch_end_effector'],
            
    #         # constraint setting
    #         'constrain_hazard3Ds': False,  # Constrain robot from being in hazardous areas
    #         'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.
            
    #         # lidar setting
    #         'lidar_num_bins': 10,
    #         'lidar_num_bins3D': 6,
    #         'lidar_body': ['link_2', 'link_5', 'link_7'],
    #         # 'lidar_body': ['link_1', 'link_3', 'link_5'],
            
    #         # object setting
    #         'hazard3Ds_num': 0,
    #         'hazard3Ds_size': 0.2,
    #         'hazard3Ds_z_range': [0.1,0.1],
            
    #         # render setting
    #         'render_lidar_radius': 0.08,
    #         'render_lidar_size': 0.015,
    #         'render_compass_radius': 0.15, 
    #         'render_compass_size': 0.03,  
    #     }
    config = {
            # robot setting
            'robot_base': 'xmls/point.xml',  

            # task setting
            'task': 'defense',
            'goal_size': 0.5,

            # observation setting
            'observe_robbers': True,  # Observe the goal with a lidar sensor
            'observe_hazards': True,  # Observe the vector from agent to hazards
            
            # constraint setting
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            # lidar setting
            'lidar_num_bins': 16,
            
            # object setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'robbers_num': 2,
            'robbers_size': 0.3,
        }
    config['num_steps']=2000
    config['robot_rot']=0
    env = Engine(config)
    obs = env.reset()
    done = False
    ep_ret = 0
    ep_cost = 0
    cnt = 0
    T = 1000
    
    # with open("link_pos.txt",'w+') as f:
    #     pos_6 = []
    #     np.savetxt(f, pos_6,  delimiter = ' ')
    ac = 10.0
    import time
    t = time.time()
    first_done = 0
    while True:
        # if done:
        #     print('Episode Return: %.3f \t Episode Cost: %.3f'%(ep_ret, ep_cost))
        #     ep_ret, ep_cost = 0, 0
        #     obs = env.reset()
        # assert env.observation_space.contains(obs)
        act = env.action_space.sample()
        # act = np.zeros(act.shape)
        # act[0] = 100*cnt
        # print(act)
        
        cnt = cnt + 1
        # print(cnt)
        # if cnt % 1000 > 50:
        #     act = np.zeros(act.shape)
        # else:
        #     act = [0.0, -0.5, -0.5] 
        # if cnt % 400 > 200:
        #     act[0] = 10.0
        #     act[1] = 10.0
        # else:
        #     act[0] = -10.0

        #     act[1] = -10.0

        # if cnt != 0:
        #     key = getkey()
        #     if key == "1":
        #         act[0] = 1.0
        #     if key == "2":
        #         act[0] = -1.0
        #     if key == "3":
        #         act[1] = 1.0
        #     if key == "4":
        #         act[1] = -1.0
        #     if key == "4":
        #         act[2] = 1.0
        #     if key == "6":
        #         act[2] = -1.0  
        # cnt = 1
        # if cnt  > 100:
        #     act = [1.0, 1.0, -1.0, -1.0]  
        # if cnt > 200:
        #     act = [1.0, 1.0, -1.0, -1.0]
        # if cnt > 300:
        #     act = [1.0, 1.0, -1.0, -1.0]
        # if cnt > 400:
        #     act = [-1.0, -1.0, 1.0, 1.0]
        # if cnt > 500:
        #     act = [-1.0, -1.0, 1.0, 1.0]
        # if cnt > 600:
        #     act = [1.0, 1.0, 1.0, 1.0]
        # if cnt > 700:
        #     act = [0.0, 0.0, 0.0, 0.0]
        # if cnt > 800:
        #     act = [0.0, 0.0, 1.0, 1.0]
        # if cnt > 900:
        #     act = [0.0, 0.0, 0.0, 0.0]
        # cnt += 1
        # print(cnt, act)
        # act = [0.0, 0.0, 0.0]
        # if cnt  > 100:
        #     act = [0.5, 0.0, 0.0] 
        # if cnt > 800:
        #     act = [0.0, 0.0, 0.0]
        # if cnt%1000 > 300:
        #     act = [-0.1, -0.1, -0.2, -0.8, -0.8, 0.0]
        #     # act = [0.0, 0.0, 0.0, 0.0, -0.8, 0.0]
        # if cnt%1000 > 500:
        #     act = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # if cnt > 500:
        #     act = [0.6, 0.0, 0.0, 0.0, 0.0, 0.0]
        # if cnt > 600:
        #     act = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # if cnt > 700:
        #     act = [0.5, 0.0, 0.0, 0.0, 0.0, 0.0]
        # if cnt > 800:
        #     act = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # if cnt > 900:
        #     act = [0.6, 0.2, -0.4, 0.0, 0.0, 0.6]

        # assert env.action_space.contains(act)
        obs, reward, done, info = env.step(act)
        
        # print(obs['accelerometer_link_2'])
        # joint = []
        # for i in range(6):
        #     joint.append(obs['jointpos_joint_'+str(i + 1)])
        # print(joint)
        print('reward', reward)
        ep_ret += reward
        a = info['cost']
        # print(info.get('cost', 0))
        ep_cost += info.get('cost', 0)
        if done:
            # import ipdb;ipdb.set_trace()
            o = env.reset()
            # import ipdb;ipdb.set_trace()
        if cnt > 10000:
            break
        env.render()
    print("##", time.time() - t)

if __name__ == '__main__':

    

    config = {
        'robot_base': 'xmls/point.xml',
        'task': 'push',
        'observe_goal_lidar': True,
        'observe_hazards': True,
        'observe_vases': True,
        'constrain_hazards': True,
        'lidar_max_dist': 3,
        'lidar_num_bins': 16,
        'hazards_num': 4,
        'vases_num': 4
    }

    env = Engine(config)
    run_random(env)

    # from gym.envs.registration import register

    # register(id='SafexpTestEnvironment-v0',
    #         entry_point='safety_gym_arm.envs.mujoco:Engine',
    #         kwargs={'config': config})
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--env', default='SafexpTestEnvironment-v0')
    # args = parser.parse_args()
    # run_random(args.env)
