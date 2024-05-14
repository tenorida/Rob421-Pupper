import numpy as np
import time
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
from src.Controller import Controller
from src.Command import Command
from src.State import BehaviorState, State
from MangDang.mini_pupper.display import Display

# Main Loop
def main():
    config = Configuration()    
    hardware_interface = HardwareInterface()
    disp = Display()
    controller = Controller(config, four_legs_inverse_kinematics)    # Initializes Controller with Kinematics
    state = State()
    state.quat_orientation = np.array([1, 0, 0, 0])    # Initial State of Oreientation, use quatenion method
    command = Command()

    disp.show_ip()  # Display the IP address on the robot's display

    movements = ["forward", "circle_left", "circle_right", "jump"]    # Defining the Movement states
    current_movement_index = 0    # Movement Count

    last_loop = time.time()
    while True:
        now = time.time()
        if now - last_loop < config.dt:
            continue

        if current_movement_index >= len(movements):
            current_movement_index = 0  # Restart the loop

        current_movement = movements[current_movement_index]

        if current_movement == "forward":
            command.horizontal_velocity = np.array([0.1, 0])  # Move forward
            state.behavior_state = BehaviorState.WALK
        elif current_movement == "circle_left":
            command.horizontal_velocity = np.array([0, 0])  # No forward/backward movement
            command.yaw_rate = 0.5  # Turn left
            state.behavior_state = BehaviorState.TROT
        elif current_movement == "circle_right":
            command.horizontal_velocity = np.array([0, 0])  # No forward/backward movement
            command.yaw_rate = -0.5  # Turn right
            state.behavior_state = BehaviorState.TROT
        elif current_movement == "jump":
            state.behavior_state = BehaviorState.JUMP  # Set Jump state 

        controller.run(state, command, disp)  # Process the current command
        hardware_interface.set_actuator_postions(state.joint_angles)  # Actuate the servos based on computed joint angles

        time.sleep(1)  # Pause for 1 sec
        current_movement_index += 1  # Move to the next action in loop

        last_loop = time.time()    # Timestamp 
        
# Main Loop Call
if __name__ == "__main__":
    main()
