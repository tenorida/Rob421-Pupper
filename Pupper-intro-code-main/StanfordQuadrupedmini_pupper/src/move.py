from Command import Command
from Controller import Controller
from State import BehaviorState, State
import numpy as np
import time
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
# from StanforQuadrupedmini_pupper.src.Kinematics import four_legs_inverse_kinematics

config = Configuration()
state = State()
command = Command()
hardware_interface = HardwareInterface()


# # Create controller
# controller = Controller(
#     config,
#     four_legs_inverse_kinematics,
# )

state.quat_orientation = np.array([1,0,0,0])

state.behavior_state = BehaviorState.TROT

command.horizontal_velocity = np.array([0.1,0])

# controller.run(state, command)
hardware_interface.set_actuator_postions(state.joint_angles)