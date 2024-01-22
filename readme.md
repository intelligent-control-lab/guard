# GUARD: **G**eneralized **U**nified S**A**fe **R**einforcement Learning **D**evelopment Benchmark

Paper link: [GUARD: A Safe Reinforcement Learning Benchmark](https://arxiv.org/abs/2305.13681)

GUARD is a highly customizable generalized benchmark with a wide variety of RL agents, tasks, and safety constraint specifications.
GUARD comprehensively covers state-of-the-art safe RL algorithms with self-contained implementations. 

**We are implementing a GPU accelerated GUARD version called GUARD-X (To Be Released on 2/5/2024)**

GUARD is composed of two main components: GUARD Safe RL library and GUARD testing suite.
Our implementation is partially inspired by [safety-gym](https://github.com/openai/safety-gym) and [spinningup](https://github.com/openai/spinningup).

Supported algorithms in the GUARD Safe RL library include:

**Unconstrained**
- [Trust Region Policy Optimization (TRPO)](https://arxiv.org/abs/1502.05477)

**End-to-end**
- [Constrained Policy Optimization (CPO)](https://arxiv.org/abs/1705.10528)
- [TRPO-Lagrangian](https://arxiv.org/abs/1902.04623)
- [TRPO-Feasible Actor Critic (FAC)](https://arxiv.org/abs/2105.10682)
- [TRPO-Interior-point Policy Optimization (IPO)](https://arxiv.org/abs/1910.09615)
- [Projection-based Constrained Policy Optimization (PCPO)](https://arxiv.org/abs/2010.03152)
- [Primal-Dual Optimization (PDO)](https://arxiv.org/abs/1512.01629) (not in paper)
- [State-wise Constrained Policy Optimization (SCPO)] (not in paper)
  - To download SCPO code, run `git submodule update --init --recursive` after cloning this repo.

**Hierarchical**
- [TRPO-Safety Layer (SL)](https://arxiv.org/abs/1801.08757)
- [TRPO-Unrolling Safety Layer (USL)](https://arxiv.org/abs/2206.08528)
- [Lyapunov-based Safe Policy Optimization (LPG)](https://arxiv.org/abs/1901.10031) (not in paper)

GUARD testing suite supports the following agents:
- Swimmer
- Ant
- Walker
- Humanoid
- Hopper
- Arm3
- Arm6
- Drone

GUARD testing suite supports the following tasks:
- Goal
<img src="https://github.com/intelligent-control-lab/guard/assets/91172531/97270fed-af6d-44e0-b246-71845aba1932" width="400"/>

- Push
<img src="https://github.com/intelligent-control-lab/guard/assets/91172531/c3b304cc-c32f-4ea5-9328-2c6e48f26a11" width="400"/>

- Chase
<img src="https://github.com/intelligent-control-lab/guard/assets/91172531/b54a50d2-fd67-4532-8560-c803de4bf269" width="400"/>

- Defense
<img src="https://github.com/intelligent-control-lab/guard/assets/91172531/03b48a0c-1d5e-4fa8-a6d7-782a475ad5e8" width="400"/>

GUARD testing suite supports the following safety constraints (obstacles):
- 3D Hazards
- Ghosts
- 3D Ghosts
- Vases
- Pillars
- Buttons
- Gremlins

Obstacles can be either trespassable/untrespassable, immovable/passively movable/actively movable, and pertained to 2D/3D spaces.
For full options, please see the paper.

---
## Installation
Install environment:
```
conda create --name venv python=3.8
conda activate venv
pip install -r requirements.txt

```

Lastly, install `safe_rl_envs` by:

```
cd safe_rl_envs
pip install -e .
```


---
## Quick Start
### 1. Environment Configuration
A set of pre-configured environments can be found in  `safe_rl_env_config.py`. Our traning process will automatically create the pre-configured environments with `--task <env name>`. 

For a complete list of pre-configured environments, see below.

To create a custom environment using the GUARD Safe RL engine, update the `safe_rl_env_config.py` with custom configurations. For example, to build an environment with a drone robot, the chase task, two dynamic targets, some 3D ghosts,  with constraints on entering the 3D ghosts areas. Add the following configuration to `safe_rl_env_config.py`:

```
if task == "Custom_Env":
  config = {
              # robot setting
              'robot_base': 'xmls/drone.xml',  

              # task setting
              'task': 'defense',
              'goal_3D': True,
              'goal_z_range': [0.5,1.5],
              'goal_size': 0.5,
              'defense_range': 2.5,

              # observation setting
              'observe_robber3Ds': True,
              'observe_ghost3Ds': True, 
              'sensors_obs': ['accelerometer', 'velocimeter', 'gyro', 'magnetometer',
                              'touch_p1a', 'touch_p1b', 'touch_p2a', 'touch_p2b',
                              'touch_p3a', 'touch_p3b', 'touch_p4a', 'touch_p4b'],
              
              # constraint setting
              'constrain_ghost3Ds': True, 
              'constrain_indicator': False, 

              # lidar setting
              'lidar_num_bins': 10,
              'lidar_num_bins3D': 6,
              
              # object setting
              'ghost3Ds_num': 8,
              'ghost3Ds_size': 0.3,
              'ghost3Ds_travel':2.5,
              'ghost3Ds_safe_dist': 1.5,
              'ghost3Ds_z_range': [0.5, 1.5],
              'robber3Ds_num': 2,
              'robber3Ds_size': 0.3,
              'robber3Ds_z_range': [0.5, 1.5],
          }
```
The custom environment can then be  used with `--task Custom_Env` in the training process below.
### 2. Benchmark Suite

An environment in the GUARD Safe RL suite is formed as a combination of a task(one of `Goal`, `Push`, `Chase` or `Defense`), a robot (one of `Point`, `Swimmer`, `Ant`, `Walker`, `Humanoid`, `Hopper`, `Arm3`, `Arm6` or `Drone`), and a type of constraints (one of `8Hazards` and `8Ghosts`, `8` is the number of constraints). Environments include:

* `Goal_{Robot}_8Hazards`: A robot must navigate to a goal while avoiding hazards.
* `Goal_{Robot}_8Ghosts`: A robot must navigate to a goal while avoiding ghosts.
* `Push_{Robot}_8Hazards`: A robot must push a box to a goal while avoiding hazards.
* `Push_{Robot}_8Ghosts`: A robot must push a box to a goal while avoiding ghosts.
* `Chase_{Robot}_8Hazards`: A robot must chase two dynamic targets while avoiding hazards.
* `Chase_{Robot}_8Ghosts`: A robot must chase two dynamic targets while avoiding ghosts.
* `Defense_{Robot}_8Hazards`: A robot must prevent two dynamic targets from entering a protected circle area while avoiding hazards.
* `Defense_{Robot}_8Ghosts`: A robot must prevent two dynamic targets from entering a protected circle area while avoiding ghosts.

(To make one of the above, make sure to substitute `Point`, `Swimmer`, `Ant`, `Walker`, `Humanoid`, `Hopper`, `Arm3`, `Arm6` or `Drone`.)


### 3. Training
Take CPO training for example:
```
cd safe_rl_lib/cpo
conda activate venv
python cpo.py --task Goal_Point_8Hazards --seed 1
```
Training logs (e.g., config, model) will be saved under `<algo>/logs/` (in the above example `cpo/logs/`).

### 4. Viualization
To test a trained RL agent on a task and save the video:
```
python cpo_video.py --model_path logs/<exp name>/<exp name>_s<seed>/pyt_save/model.pt --task <env name> --video_name <video name> --max_epoch <max epoch>            
```
To plot training statistics (e.g., reward, cost), copy the all desired log folders to `comparison/` and then run the plot script as follows:
```
cd safe_rl_lib
mkdir comparison
cp -r <algo>/logs/<exp name> comparison/
python utils/plot.py comparison/ --title <title name> --reward --cost
```

\<title name\> can be anything that describes the current comparison (e.g., "all end-to-end methods").


## Contributing to GUARD

Welcome to GUARD! We appreciate your interest in contributing to this project. Whether you want to report a bug, suggest a feature, or contribute code, please follow the guidelines outlined below.

### Issues and Bugs

If you encounter any issues or find a bug, please open an issue on the [issue tracker](https://github.com/intelligent-control-lab/guard/issues). When reporting a bug, include a detailed description, steps to reproduce, and your system configuration.

### Feature Requests

If you have a feature request, please open an issue on the [issue tracker](https://github.com/intelligent-control-lab/guard/issues). Clearly describe the new feature you'd like to see and why it would be valuable.

### Pull Requests

We welcome contributions! If you'd like to contribute code, follow these steps:

1. Fork the repository and create a new branch.
2. Make your changes and test them thoroughly.
3. Ensure your code follows the existing code style and conventions.
4. Write clear and concise commit messages explaining your changes.
5. Open a pull request, linking to any relevant issues and providing a detailed description of your changes.

### Coding Guidelines and Style of Conventions

- Follow the [coding style guide](CODE_OF_CONDUCT.md) of the project.
- Adhere to [PEP 8 style guidelines](https://peps.python.org/pep-0008/) for Python code.
- Use descriptive variable and function names. For example, (i) ```mlp``` stands for ```Multilayer Perceptron```, (ii) ```_d_kl()``` stands for ```KL Divergence computation function```.
- Add comments to explain complex function using the following formats.
```python
def func1(arg1, arg2)
    """
    Introduction of this function.
    Additional detailed description.
    """
```

```python
def func2(arg1, arg2)
    '''Description of this function'''
```
- Write clear and concise commit messages.


### Code Reviews
- All pull requests will be reviewed by project maintainers.
- Be prepared to address any feedback or questions from reviewers.

### Additional Tips
- Before starting work on a major feature, discuss it with the maintainers first to ensure it aligns with the project's goals.
- Break down large changes into smaller, more manageable pull requests.
- Be patient and respectful during the code review process.
- Thank you for your interest in contributing to GUARD!



## Maintaining and Expanding GUARD

To ensure the long-term maintenance and growth of this code repository, we have outlined the following plan:

### Maintenance

**Regular Updates:**
We are committed to keeping GUARD up-to-date with the latest advancements in (i) [Mujoco Simulation Engine](https://mujoco.readthedocs.io/en/stable/overview.html); (ii) [Pytorch Toolbox](https://pytorch.org/) and addressing any potential issues. Regular updates will include bug fixes, feature improvements, and compatibility with new dependencies.

**Responsive Issue Management:**
We encourage users to submit issues for bugs, feature requests, or general feedback. Our team will actively monitor the [issue tracker](https://github.com/intelligent-control-lab/guard/issues) and respond promptly to address reported problems or discuss proposed enhancements.


### Expansion

#### Other Environments

You can easily change the algorithm runtime environment to another environment library that **supports the gym interface** by following these steps：

- Add necessary paramaters for build external environment to parameter `arg` in main. (Optional) 
- Import the desired environment and initialize it in `create_env` function.

#### New Features

We welcome contributions that introduce new features or improvements to existing ones. If you have ideas for enhancing Safety Gym, please open an issue to discuss the proposed changes before submitting a pull request.

#### Community Involvement

We aim to build a vibrant community around Safety Gym. Contributions from the community, including code submissions, bug reports, and feature requests, are crucial for the project's growth. Engage with the community through discussions, forums, and collaborative efforts.

#### Documentation

Maintaining comprehensive and up-to-date documentation is key to the usability of Safety Gym. We encourage contributors to document new features and help improve existing documentation.

### Roadmap

We have outlined a roadmap for the future development of Safety Gym, which can be found in the [ROADMAP.md](link_to_your_roadmap_file). This document provides insights into upcoming features, milestones, and goals for the project.

### Feedback and Suggestions

We welcome feedback and suggestions on how we can improve this maintenance and expansion plan. Feel free to open an issue to share your thoughts and ideas.



---
## Citing GUARD
```
@article{zhao2023guard,
  title={GUARD: A Safe Reinforcement Learning Benchmark},
  author={Zhao, Weiye and Chen, Rui and Sun, Yifan and Li, Feihan and Liu, Ruixuan and Wei, Tianhao and Liu, Changliu},
  journal={arXiv preprint arXiv:2305.13681},
  year={2023}
}
```

