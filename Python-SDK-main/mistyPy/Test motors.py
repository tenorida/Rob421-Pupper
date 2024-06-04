import sys, os
from time import sleep
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

ROBOT_IP = "192.168.0.103"  # replace with your correct IP
STOP_DISTANCE = 0.3  # distance [m]] to stop the robot

misty_robot = Robot(ROBOT_IP)

misty_robot.drive_track(leftTrackSpeed=-60, rightTrackSpeed=-20)
time.sleep(5)
misty_robot.drive_track(leftTrackSpeed=30, rightTrackSpeed=30)

misty_robot.keep_alive()
