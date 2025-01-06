import os

GUARD_ENV_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
import safe_rl_envs.envs
from safe_rl_envs.xmls.g1.deploy_mujoco import G1Controller