import sys
import os
import time
from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

ROBOT_IP = "192.168.0.101"  # replace with your correct IP
STOP_DISTANCE = 0.3  # distance [m] to stop the robot

misty_robot = Robot(ROBOT_IP)


def stop_robot():
    misty_robot.stop()


# Sense "obstacle" and move accordingly
def move_away_from_obstacle(sensor_id):
    misty_robot.stop()
    if sensor_id == "toffc":
        print(f"Moving backward to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive_track(leftTrackSpeed=-40, rightTrackSpeed=-40)
        time.sleep(2)
    elif sensor_id == "toffr":
        print(f"Turning left to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive_track(leftTrackSpeed=-20, rightTrackSpeed=-60)
        time.sleep(2)
    elif sensor_id == "toffl":
        print(f"Turning right to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive_track(leftTrackSpeed=-60, rightTrackSpeed=-20)
        time.sleep(2)
    misty_robot.stop()


def tof_callback(message):
    distance = message["message"]["distanceInMeters"]
    sensor_id = message["message"]["sensorId"]
    if distance < STOP_DISTANCE:
        print(f"Object detected by {sensor_id} within {STOP_DISTANCE} meters. Stopping robot.")
        move_away_from_obstacle(sensor_id)
    else:
        print(f"Path clear. Continuing forward.")
        misty_robot.drive_track(leftTrackSpeed=30, rightTrackSpeed=30)


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
            Events.TimeOfFlight, "frontleft", condition=[EventFilters.TimeOfFlightPosition.FrontLeft],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )

        misty_robot.drive_track(leftTrackSpeed=30, rightTrackSpeed=30)

        # Keep the main thread alive
        misty_robot.keep_alive()

    except Exception as ex:
        print(ex)
    finally:
        # Unregister from all events to clean up
        misty_robot.unregister_all_events()
