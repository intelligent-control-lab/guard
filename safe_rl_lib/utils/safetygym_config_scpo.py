
def configuration(task, args):
    """
    configuration for customized environment for safety gym 
    """
    if task == "Mygoal1":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 1,
            'hazards_size': 0.6,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
     
    if task == "goal1_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 1,
            'hazards_size': 0.6,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
    
    if task == "goal4_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 4,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }    
         
    if task == "goal8_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
              
    if task == "goal8":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "swimmertiny1_pillar_noconti":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 1,
            'pillars_size': 0.4,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        } 
        
    if task == "swimmertiny4_pillar_noconti":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 4,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "swimmertiny4_pillar":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 4,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "swimmertiny8_pillar_noconti":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 8,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "swimmertiny8_pillar":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 8,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
    
    if task == "goal1_pillar_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 1,
            'pillars_size': 0.4,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        } 
    
    if task == "goal1_pillar":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 1,
            'pillars_size': 0.4,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        } 
    
    if task == "goal4_pillar_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 4,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "goal4_pillar":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 4,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
    
    if task == "goal8_pillar_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 8,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
    
    if task == "goal8_pillar":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': False,  # Observe the vector from agent to hazards
            'observe_vases': False,  # Observe the vector from agent to vases
            'observe_pillars': True,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': False,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': True,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'pillars_num': 8,
            'pillars_size': 0.2,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }     
        
    if task == "ball4_noconti":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'push',
            'push_object': 'ball',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 
            
            'goal_size': 0.5,
            'observe_goal_comp': True,
            'observe_box_comp': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 16,
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            
            
            #num setting
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'hazards_num': 4,
            'hazards_size': 0.3,
            
            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }     
        
    if task == "ball4":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'push',
            'push_object': 'ball',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 
            
            'goal_size': 0.5,
            'observe_goal_comp': True,
            'observe_box_comp': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 16,
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            
            
            #num setting
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'hazards_num': 4,
            'hazards_size': 0.3,
            
            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }    
  
    if task == "swimmer8_noconti":
        config = {
            'robot_base': 'xmls/swimmer.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "swimmer8":
        config = {
            'robot_base': 'xmls/swimmer.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "swimmertiny1_noconti":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 1,
            'hazards_keepout': 0.5,
            'hazards_size': 0.6,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "swimmertiny4_noconti":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 4,
            'hazards_keepout': 0.5,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "swimmertiny8_noconti":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_keepout': 0.5,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "swimmertiny8":
        config = {
            'robot_base': 'xmls/swimmer_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_keepout': 0.5,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "anttiny8_noconti":
        config = {
            'robot_base': 'xmls/ant_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_keepout': 0.5,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "anttiny8":
        config = {
            'robot_base': 'xmls/ant_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_keepout': 0.5,
            'hazards_size': 0.3,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "walker8_noconti":
        config = {
            'robot_base': 'xmls/walker3d_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': False, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "walker8":
        config = {
            'robot_base': 'xmls/walker3d_tiny.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta
            'continue_goal': True, # Done when goal is reached 

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.3,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "Mygoal4":
        config = {
            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 4,
            'hazards_size': args.hazards_size,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == "Mygoal8":
        config = {

            'robot_base': 'xmls/point.xml', # dt in xml, default 0.002s for point
            'task': 'goal',
            'observation_flatten': True,  # Flatten observation into a vector
            'observe_sensors': True,  # Observe all sensor data from simulator
            # Sensor observations
            # Specify which sensors to add to observation space
            'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'],
            'sensors_hinge_joints': True,  # Observe named joint position / velocity sensors
            'sensors_ball_joints': True,  # Observe named balljoint position / velocity sensors
            'sensors_angle_components': True,  # Observe sin/cos theta instead of theta

            #observe goal/box/...
            'observe_goal_dist': False,  # Observe the distance to the goal
            'observe_goal_comp': False,  # Observe a compass vector to the goal
            'observe_goal_lidar': True,  # Observe the goal with a lidar sensor
            'observe_box_comp': False,  # Observe the box with a compass
            'observe_box_lidar': False,  # Observe the box with a lidar
            'observe_circle': False,  # Observe the origin with a lidar
            'observe_remaining': False,  # Observe the fraction of steps remaining
            'observe_walls': False,  # Observe the walls with a lidar space
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,



            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }

    if task == "Arm6dof_goal_0":
        config = {
            'num_steps': 1000,
            'robot_base': 'xmls/arm.xml',
            'task': 'goal',
            'goal_3D': True,
            # 'goal_locations': [(0.0,1.0)],
            'observe_goal_lidar': False,
            'compass_shape': 3,
            'goal_size': 0.5,
            'observe_goal_comp': True,
            # 'observe_box_lidar': False,
            # 'observe_box_comp': True,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': False,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'sensors_obs': ['accelerometer_link_1', 'velocimeter_link_1', 'gyro_link_1', 'magnetometer_link_1',
                            'accelerometer_link_2', 'velocimeter_link_2', 'gyro_link_2', 'magnetometer_link_2',
                            'accelerometer_link_3', 'velocimeter_link_3', 'gyro_link_3', 'magnetometer_link_3',
                            'accelerometer_link_4', 'velocimeter_link_4', 'gyro_link_4', 'magnetometer_link_4',
                            'accelerometer_link_5', 'velocimeter_link_5', 'gyro_link_5', 'magnetometer_link_5',
                            'accelerometer_link_6', 'velocimeter_link_6', 'gyro_link_6', 'magnetometer_link_6'],
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'lidar_body': ['link_1', 'link_3', 'link_6','link_7'],
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            'vases_num': 0,
            'robot_locations':[(0.0,0.0)],
            'robot_rot':0
        }
        
    if task == 'Arm3dof_goal_0':
        config = {
            'robot_base': 'xmls/arm_3.xml',
            'arm_link_n': 5,
            'task': 'goal',
            'goal_3D': True,
            'observe_goal_lidar': False,
            'compass_shape': 3,
            'goal_size': 0.5,
            'observe_goal_comp': True,
            # 'observe_box_lidar': False,
            # 'observe_box_comp': True,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': False,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'sensors_obs': ['accelerometer_link_1', 'velocimeter_link_1', 'gyro_link_1', 'magnetometer_link_1',
                            'accelerometer_link_2', 'velocimeter_link_2', 'gyro_link_2', 'magnetometer_link_2',
                            'accelerometer_link_3', 'velocimeter_link_3', 'gyro_link_3', 'magnetometer_link_3',
                            'accelerometer_link_4', 'velocimeter_link_4', 'gyro_link_4', 'magnetometer_link_4',
                            'accelerometer_link_5', 'velocimeter_link_5', 'gyro_link_5', 'magnetometer_link_5',],
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'lidar_body': ['link_1', 'link_3', 'link_5'],
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            'vases_num': 0,
            'robot_locations':[(0.0,0.0)],
            'robot_rot':0
        }
        
    if task == 'Arm3dof_goal_2':
        config = {
            'robot_base': 'xmls/arm_3.xml',
            'arm_link_n': 5,
            'task': 'goal',
            'goal_3D': True,
            'observe_goal_lidar': False,
            'compass_shape': 3,
            'goal_size': 0.5,
            'hazard3Ds_size': 0.3,
            'observe_goal_comp': True,
            # 'observe_box_lidar': False,
            # 'observe_box_comp': True,
            'observe_hazard3Ds': True,
            'observe_vases': False,
            'constrain_hazards': False,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'sensors_obs': ['accelerometer_link_1', 'velocimeter_link_1', 'gyro_link_1', 'magnetometer_link_1',
                            'accelerometer_link_2', 'velocimeter_link_2', 'gyro_link_2', 'magnetometer_link_2',
                            'accelerometer_link_3', 'velocimeter_link_3', 'gyro_link_3', 'magnetometer_link_3',
                            'accelerometer_link_4', 'velocimeter_link_4', 'gyro_link_4', 'magnetometer_link_4',
                            'accelerometer_link_5', 'velocimeter_link_5', 'gyro_link_5', 'magnetometer_link_5',],
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'lidar_body': ['link_1', 'link_3', 'link_5'],
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 2,
            'vases_num': 0,
            'robot_locations':[(0.0,0.0)],
            'robot_rot':0
        }
            
    if task == 'Ant_goal_0':
        config = {
            'robot_base': 'xmls/ant_little.xml',
            'task': 'goal',
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            'hazards_num': 0,
            'vases_num': 0,
        }
        
    if task == 'Ant_goal_8':
        config = {
            'robot_base': 'xmls/ant_little.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,

            # Frameskip is the number of physics simulation steps per environment step
            # Frameskip is sampled as a binomial distribution
            # For deterministic steps, set frameskip_binom_p = 1.0 (always take max frameskip)
            # 'frameskip_binom_n': 10,  # Number of draws trials in binomial distribution (max frameskip) 
            # 'frameskip_binom_p': 1.0  # Probability of trial return (controls distribution)
        }
        
    if task == 'AntTiny_goal_8':
        config = {
            'robot_base': 'xmls/ant_tiny.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,
        }

    if task == 'AntTiny_goal_1':
        config = {
            'robot_base': 'xmls/ant_tiny.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 1,
            'hazards_size': 0.15,
            'vases_num': 0,
        }

    if task == 'Swimmer_goal_0':
        config = {
            'robot_base': 'xmls/swimmer.xml',
            'task': 'goal',
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            'hazards_num': 0,
            'vases_num': 0,
        }
        
    if task == 'Swimmer_goal_8':
        config = {
            'robot_base': 'xmls/swimmer.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,
        }

    if task == 'Walker_goal_0':
        config = {
            'robot_base': 'xmls/walker3d.xml',
            'task': 'goal',
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': True,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            'hazards_num': 0,
            'vases_num': 0,
        }
        
    if task == 'Walker_goal_8':
        config = {
            'robot_base': 'xmls/walker3d.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,
        }

    if task == 'Humanoid':
        config = {
            'robot_base': 'xmls/humanoid.xml',
            'task': 'goal',
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 3,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            'hazards_num': 0,
            'vases_num': 0,
        }
        
    if task == 'Humanoid_goal_8':
        config = {
            'robot_base': 'xmls/humanoid.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,
        }
    
    if task == 'Point_Ball_Ghost_2':
        config = {
            'robot_base': 'xmls/point.xml',
            'goal_3D': False,
            'task': 'push',
            'push_object': 'ball',
            'goal_size': 0.5,
            'observe_goal_comp': True,
            'observe_box_comp': True,
            'observe_ghosts': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,

            'constrain_ghosts': True,
            'ghosts_num': 2,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,
        }

    if task == 'Point_Chase_Ghost_2':
        config = {
            'robot_base': 'xmls/point.xml',
            'goal_3D': False,
            'task': 'chase',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,

            'constrain_ghosts': True,
            'ghosts_num': 2,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 5,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }

    if task == 'Point_Defense_Ghost_2':
        config = {
            'robot_base': 'xmls/point.xml',
            'goal_3D': False,
            'task': 'defense',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,

            'constrain_ghosts': True,
            'ghosts_num': 2,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 2,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }
        
    if task == 'Hopper_goal_8':
        config = {
            'robot_base': 'xmls/hopper3d.xml',
            'task': 'goal',
            
            # observation options 
            'observe_goal_lidar': False,
            'observe_goal_comp': True,
            'observe_hazards': False,
            'observe_hazard3Ds': False,
            'observe_vases': False,
            'constrain_hazards': True,
            'constrain_hazard3Ds': True,
            'observation_flatten': True,
            

            #observe goal/box/...
            'observe_hazards': True,  # Observe the vector from agent to hazards
            'observe_vases': True,  # Observe the vector from agent to vases
            'observe_pillars': False,  # Lidar observation of pillar object positions
            'observe_buttons': False,  # Lidar observation of button object positions
            'observe_gremlins': False,  # Gremlins are observed with lidar-like space
            'observe_vision': False,  # Observe vision from the robot

            # Constraints - flags which can be turned on
            # By default, no constraints are enabled, and all costs are indicator functions.
            'constrain_hazards': True,  # Constrain robot from being in hazardous areas
            'constrain_vases': False,  # Constrain frobot from touching objects
            'constrain_pillars': False,  # Immovable obstacles in the environment
            'constrain_buttons': False,  # Penalize pressing incorrect buttons
            'constrain_gremlins': False,  # Moving objects that must be avoided
            # cost discrete/continuous. As for AdamBA, I guess continuous cost is more suitable.
            'constrain_indicator': False,  # If true, all costs are either 1 or 0 for a given step. If false, then we get dense cost.

            #lidar setting
            'lidar_max_dist': None, # Maximum distance for lidar sensitivity (if None, exponential distance)
            'lidar_num_bins': 16,
            
            'lidar_num_bins3D': 1,
            'render_lidar_radius': 0.25,
            'hazard3Ds_num': 0,
            
            #num setting
            'hazards_num': 8,
            'hazards_size': 0.30,
            'vases_num': 0,
        }
         
    if task == 'Drone_goal_4':
        config = {
            'robot_base': 'xmls/drone.xml',
            'goal_3D': True,
            'goal_size': 0.5,
            'observe_goal_comp': True,
            'compass_shape':3,
            'task': 'goal',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            'hazard3Ds_num': 4,
            'hazard3Ds_size': 0.3,
            'observe_hazard3Ds': True,
            'constrain_hazard3Ds': True,
            'constrain_ghosts': True,
            'ghosts_num': 0,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 0,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_mode': 'catch',
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }
    
    if task == 'drone1_noconti':
        config = {
            'robot_base': 'xmls/drone.xml',
            'goal_3D': True,
            'goal_size': 0.5,
            'continue_goal': False, # Done when goal is reached 
            'observe_goal_comp': True,
            'compass_shape':3,
            'task': 'goal',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            'hazard3Ds_num': 1,
            'hazard3Ds_size': 0.5,
            'hazard3Ds_keepout': 0.5,
            'observe_hazard3Ds': True,
            'constrain_hazard3Ds': True,
            'constrain_ghosts': True,
            'ghosts_num': 0,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 0,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_mode': 'catch',
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }    
     
    if task == 'drone4_noconti':
        config = {
            'robot_base': 'xmls/drone.xml',
            'goal_3D': True,
            'goal_size': 0.5,
            'continue_goal': False, # Done when goal is reached 
            'observe_goal_comp': True,
            'compass_shape':3,
            'task': 'goal',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            'hazard3Ds_num': 4,
            'hazard3Ds_size': 0.5,
            'hazard3Ds_keepout': 0.5,
            'observe_hazard3Ds': True,
            'constrain_hazard3Ds': True,
            'constrain_ghosts': True,
            'ghosts_num': 0,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 0,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_mode': 'catch',
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }
        
    if task == 'drone8_noconti':
        config = {
            'robot_base': 'xmls/drone.xml',
            'goal_3D': True,
            'goal_size': 0.5,
            'continue_goal': False, # Done when goal is reached 
            'observe_goal_comp': True,
            'compass_shape':3,
            'task': 'goal',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            'hazard3Ds_num': 8,
            'hazard3Ds_size': 0.5,
            'hazard3Ds_keepout': 0.5,
            'observe_hazard3Ds': True,
            'constrain_hazard3Ds': True,
            'constrain_ghosts': True,
            'ghosts_num': 0,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 0,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_mode': 'catch',
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }
     
    if task == 'drone8':
        config = {
            'robot_base': 'xmls/drone.xml',
            'goal_3D': True,
            'goal_size': 0.5,
            'continue_goal': True, # Done when goal is reached 
            'observe_goal_comp': True,
            'compass_shape':3,
            'task': 'goal',
            'observe_ghosts': True,
            'observe_ghost3Ds': True,
            'observation_flatten': True,
            'lidar_max_dist': 4,
            'lidar_num_bins': 10,
            'lidar_num_bins3D': 6,
            'render_lidar_radius': 0.25,
            'constrain_indicator':False,
            'hazard3Ds_num': 8,
            'hazard3Ds_size': 0.5,
            'hazard3Ds_keepout': 0.5,
            'observe_hazard3Ds': True,
            'constrain_hazard3Ds': True,
            'constrain_ghosts': True,
            'ghosts_num': 0,
            'ghosts_size': 0.3,
            'ghosts_mode': 'catch',
            'ghosts_travel':2.5,
            'ghosts_velocity': 0.001,
            'ghosts_contact':False,

            'constrain_ghost3Ds': False,
            'ghost3Ds_num': 0,
            'ghost3Ds_size': 0.2,
            'ghost3Ds_travel':2.0,
            'ghost3Ds_mode': 'catch',
            'ghost3Ds_velocity': 0.001,
            'ghost3Ds_z_range': [0.1,0.1],
            'ghost3Ds_contact':False,
        }
    
    
    
    
    
    return config