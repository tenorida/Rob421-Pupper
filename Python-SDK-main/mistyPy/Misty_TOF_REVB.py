import sys, os
from time import sleep
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

ROBOT_IP = "192.168.0.102"  # replace with your correct IP
STOP_DISTANCE = 0.1  # distance [m]] to stop the robot

misty_robot = Robot(ROBOT_IP)
processing_trigger = False

def stop_robot():
    misty_robot.stop()



#sense "obstacle" and move accordingly
def move_away_from_obstacle(sensor_id):
    misty_robot.stop()
    global processing_trigger

    if "toffc" in sensor_id:
        print(f"Moving backward to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(linearVelocity=-10, angularVelocity=5)
        time.sleep(5)
        misty_robot.drive(linearVelocity=10, angularVelocity=0)

    elif "tofr" in sensor_id:
        #print(f"Moving forward to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(10, 0)
        time.sleep(2)
        misty_robot.drive(linearVelocity=10, angularVelocity=0)

    elif "toffl" in sensor_id:
        #print(f"Moving back and left to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(linearVelocity=-10, angularVelocity=-20) #Left
        time.sleep(3)
        misty_robot.stop()
        misty_robot.drive(linearVelocity=10, angularVelocity=0)

    elif "toffr" in sensor_id:
        #print(f"Moving back and right to avoid obstacle detected by {sensor_id}.")
        misty_robot.drive(linearVelocity=-10, angularVelocity=25) #right
        time.sleep(3)
        misty_robot.stop()
        misty_robot.drive(linearVelocity=10, angularVelocity=0) 
    processing_trigger = False    

def tof_callback(message):
    global processing_trigger
    if processing_trigger:
        return  # Ignore sensor triggers while processing another one
    
    distance = message["message"]["distanceInMeters"]
    sensor_id = message["message"]["sensorId"]
    if distance < STOP_DISTANCE:
        print(f"Object detected by {sensor_id} within {STOP_DISTANCE} meters. Stopping robot.")
        processing_trigger = True
        move_away_from_obstacle(sensor_id)
        time.sleep(3)
    else:
        print(f"Moving forward")
        misty_robot.drive(linearVelocity=15, angularVelocity=0)
        

if __name__ == "__main__":
    try:
        print("main loop")
        #Subscribe to the front ToF sensors
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
        '''back_center = misty_robot.register_event(
            Events.TimeOfFlight, "backcenter", condition=[EventFilters.TimeOfFlightPosition.Back], keep_alive=True,
            callback_function=tof_callback, debounce=0
        )'''         
        #misty_robot.drive(linearVelocity=-10, angularVelocity=20) #Left
        #time.sleep(3)
        #misty_robot.stop()
        #misty_robot.drive(linearVelocity=-10, angularVelocity=-25) #Rights
        #time.sleep(3)
        #misty_robot.stop()
        misty_robot.drive(linearVelocity=10, angularVelocity=0) # Foward
        #time.sleep(3)
        #misty_robot.stop()
    
        
        # misty_robot.start_object_detector()
        # def recognized(data):

        #     print(data)
        #     object  is for testing
        #     if data["message"]["description"] == 'person':
        #         misty_robot.stop()
        #         time.sleep(1)
        #         misty_robot.play_audio("s_Awe.wav", 20)
        #         time.sleep(1)
        #         misty_robot.speak("I love humans, they are my best friends")
        #         misty_robot.transition_led(0, 255, 0, 255, 255, 0, "TransitOnce", 1000)

        misty_robot.start_object_detector()
        def recognized(data):
            print(data)  
            
            if data["message"]["description"] == 'person':
                misty_robot.stop()
                time.sleep(1)
                misty_robot.play_audio("s_Awe.wav", 50)
                time.sleep(1)
                misty_robot.speak("I love humans, they are my best friends", volume = 50)
                misty_robot.transition_led(0, 255, 0, 255, 255, 0, "TransitOnce", 1000)
            elif data["message"]["description"] == 'backpack':
                time.sleep(1)
                misty_robot.play_audio("s_rage.wav")
                time.sleep(1)
                misty_robot.speak("That's a backpack I am now angry")
                misty_robot.transition_led(255, 0, 0, 255, 127, 0, "TransitOnce", 1000)
            # elif data["message"]["description"] == 'box':
            #     time.sleep(1)
            #     misty_robot.play_audio("s_Sadness.wav")
            #     time.sleep(1)
            #     misty_robot.speak("the box is in my way, I will go around the box")
            #     misty_robot.transition_led(255, 0, 255, 0, 0, 0, "TransitOnce", 1000)
        misty_robot.register_event(event_name='object_detection_event', event_type=Events.ObjectDetection, callback_function=recognized, keep_alive=False)
        
        # Use the keep_alive() function to keep the main thread alive
        misty_robot.keep_alive()

    except Exception as ex:
        print(ex)
    finally:
        # Unregister from all events to clean up
        misty_robot.unregister_all_events()
