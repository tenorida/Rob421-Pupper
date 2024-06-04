import sys
import os
import time
from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

ROBOT_IP = "192.168.0.100"  # replace with correct IP
STOP_DISTANCE = 0.3  # distance [m] to stop the robot

misty_robot = Robot(ROBOT_IP)

def stop_robot():
    misty_robot.stop()

# Sense obstacle and do move correctly
def move_away_from_obstacle(sensor_id):
    if sensor_id == "toffc":
        print(f"Moving backward to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(linearVelocity=-10, angularVelocity=0)
        time.sleep(5)
    elif sensor_id == "tofr":
        print(f"Turning left to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(linearVelocity=-10, angularVelocity=-25)  # Right
        time.sleep(3)
    elif sensor_id == "toffl":
        print(f"Turning right to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(linearVelocity=-10, angularVelocity=25)  # Left
        time.sleep(3)
    misty_robot.drive(linearVelocity=10, angularVelocity=0)

# Define a priority order for sensors
SENSOR_PRIORITY = ["toffc", "tofr", "toffl"]

def tof_callback(message):
    distance = message["message"]["distanceInMeters"]
    sensor_id = message["message"]["sensorId"]
    print(f"Sensor {sensor_id} detected an object at {distance:.2f} meters.")
    
    if distance < STOP_DISTANCE:
        print(f"Object detected by {sensor_id} within {STOP_DISTANCE} meters. Stopping robot.")
        if sensor_id in SENSOR_PRIORITY:
            move_away_from_obstacle(sensor_id)
        time.sleep(3)
    else:
        print(f"Path clear. Continuing forward.")
        misty_robot.drive(linearVelocity=15, angularVelocity=0)

if __name__ == "__main__":
    try:
        print("Main loop started")
        # Subscribe to the front ToF sensors
        misty_robot.register_event(
            Events.TimeOfFlight, "frontright", condition=[EventFilters.TimeOfFlightPosition.FrontRight],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )
        misty_robot.register_event(
            Events.TimeOfFlight, "frontcenter", condition=[EventFilters.TimeOfFlightPosition.FrontCenter],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )
        misty_robot.register_event(
            Events.TimeOfFlight, "frontleft", condition=[EventFilters.TimeOfFlightPosition.FrontLeft],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )

        misty_robot.drive(linearVelocity=10, angularVelocity=0)  # Forward

        # Keep the main thread alive
        misty_robot.keep_alive()

    except Exception as ex:
        print(ex)
    finally:
        # Unregister from all events to clean up
        misty_robot.unregister_all_events()
