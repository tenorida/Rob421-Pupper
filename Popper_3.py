import numpy as np
import time
from src.IMU import IMU
from src.Controller import Controller
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
from MangDang.mini_pupper.display import Display
from src.State import State
from src.MovementScheme import MovementScheme
from src.danceSample import MovementLib

def main(use_imu=False):
    """ main program to move the robot forward and stop for 5 sec """

    # Initialize Config and Hardware
    config = Configuration()
    hardware_interface = HardwareInterface()
    disp = Display()
    # disp.show_ip()

    # IMU - Do we need this?
    if use_imu:
        imu = IMU(port="/dev/ttyACM0")
        imu.flush_buffer()

    # Controller with the inverse kinematics function
    controller = Controller(config, four_legs_inverse_kinematics)
    state = State()

    # Start Movement Scheme
    movementCtl = MovementScheme(MovementLib)

    # Moving forward
    print("Robot moving forward...")
    movementCtl.runMovementScheme()  # Is this predefined forward movement ? - Please check
    legsLocation = movementCtl.getMovemenLegsLocation() # Is this correct implementation for Leg Location?
    attitudes = movementCtl.getMovemenAttitude()
    speed = movementCtl.getMovemenSpeed()
    controller.run(state, None, disp, legsLocation, attitudes, speed)

    # Simulate forward for 5 sec
    time.sleep(5)

    # Stop
    print("Stopping robot...")
    hardware_interface.set_actuator_postions(np.zeros_like(state.joint_angles))  # Reset all servos

    print("Robot movement completed.")

if __name__ == "__main__":
    main(use_imu=True)
