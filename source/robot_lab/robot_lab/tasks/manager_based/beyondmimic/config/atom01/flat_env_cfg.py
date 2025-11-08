# Copyright (c) 2024-2025 Ziqi Fan
# SPDX-License-Identifier: Apache-2.0

import os

from isaaclab.utils import configclass

from robot_lab.assets.unitree import UNITREE_G1_29DOF_ACTION_SCALE, UNITREE_G1_29DOF_CFG
from robot_lab.assets.roboparty import ATOM01_CFG
from robot_lab.tasks.manager_based.beyondmimic.tracking_env_cfg import BeyondMimicEnvCfg


@configclass
class Atom01BeyondMimicFlatEnvCfg(BeyondMimicEnvCfg):
    def __post_init__(self):
        super().__post_init__()

        self.scene.robot = ATOM01_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.actions.joint_pos.scale = 0.25
        self.commands.motion.motion_file = f"{os.path.dirname(__file__)}/motion/dance.npz"
        self.commands.motion.anchor_body_name = "torso_link"
        self.commands.motion.body_names = [
            'base_link',
            'left_thigh_roll_link',
            'left_knee_link',
            'left_ankle_roll_link',
            'right_thigh_roll_link',
            'right_knee_link',
            'right_ankle_roll_link',
            'torso_link',
            'left_arm_yaw_link',
            'left_elbow_pitch_link',
            'left_elbow_yaw_link',
            'right_arm_yaw_link',
            'right_elbow_pitch_link',
            'right_elbow_yaw_link'
        ]

        self.episode_length_s = 15.0
