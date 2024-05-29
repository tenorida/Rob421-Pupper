import sys, os
from time import sleep
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

ROBOT_IP = "192.168.0.102"  # replace with your correct IP
STOP_DISTANCE = 0.2  # distance [m]] to stop the robot

misty_robot = Robot(ROBOT_IP)

def stop_robot():
    misty_robot.stop()

def move_away_from_obstacle(sensor_id):
    if "front" in sensor_id:
        print(f"Moving backward to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive_time(linear_velocity=-40, angular_velocity=0, time_ms=1000)
    elif "back" in sensor_id:
        print(f"Moving forward to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive_time(linear_velocity=40, angular_velocity=0, time_ms=1000)

def tof_callback(message):
    distance = message["message"]["distanceInMeters"]
    sensor_id = message["message"]["sensorId"]
    if distance < STOP_DISTANCE:
        print(f"Object detected by {sensor_id} within {STOP_DISTANCE} meters. Stopping robot.")
        stop_robot()
        move_away_from_obstacle(sensor_id)

if __name__ == "__main__":
    try:
        # Subscribe to the front ToF sensors
        front_right = misty_robot.register_event(
            Events.TimeOfFlight, "frontright", condition=[EventFilters.TimeOfFlightPosition.FrontRight],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )
        front_center = misty_robot.register_event(
            Events.TimeOfFlight, "frontcenter", condition=[EventFilters.TimeOfFlightPosition.FrontCenter],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )
        front_left = misty_robot.register_event(
            Events.TimeOfFlight, "frontleft", condition=[EventFilters.TimeOfFlightPosition.FrontLeft], keep_alive=True,
            callback_function=tof_callback, debounce=0
        )

        # Subscribe to the back ToF sensors
        # back_right = misty_robot.register_event(
        #     Events.TimeOfFlight, "backright", condition=[EventFilters.TimeOfFlightPosition.BackRight], keep_alive=True,
        #     callback_function=tof_callback, debounce=0
        # )
        back_center = misty_robot.register_event(
            Events.TimeOfFlight, "backcenter", condition=[EventFilters.TimeOfFlightPosition.Back], keep_alive=True,
            callback_function=tof_callback, debounce=0
        )
        # back_left = misty_robot.register_event(
        #     Events.TimeOfFlight, "backleft", condition=[EventFilters.TimeOfFlightPosition.BackLeft], keep_alive=True,
        #     callback_function=tof_callback, debounce=0
        # )

        # Use the keep_alive() function to keep the main thread alive
        misty_robot.keep_alive()

    except Exception as ex:
        print(ex)
    finally:
        # Unregister from all events to clean up
        misty_robot.unregister_all_events()