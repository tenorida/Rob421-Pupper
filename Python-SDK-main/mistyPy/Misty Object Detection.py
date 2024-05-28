from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time 

ipAddress = "192.168.0.102"
misty = Robot(ipAddress)

misty.StartObjectDetector()
def recognized(data):
    print(data)  
    
    if data["message"]["description"] == 'person':
        time.sleep(1)
        misty.PlayAudio("s_Awe.wav", 20)
        time.sleep(1)
        misty.Speak("I love humans, they are my best friends")
        misty.TransitionLED(0, 255, 0, 255, 255, 0, "TransitOnce", 1000)
    elif data["message"]["description"] == 'chair':
        time.sleep(1)
        misty.PlayAudio("s_rage.wav")
        time.sleep(1)
        misty.Speak("That's a chair I am now angry")
        misty.TransitionLED(255, 0, 0, 255, 127, 0, "TransitOnce", 1000)
    elif data["message"]["description"] == 'box':
        time.sleep(1)
        misty.PlayAudio("s_Sadness.wav")
        time.sleep(1)
        misty.Speak("the box is in my way, I will go around the box")
        misty.TransitionLED(255, 0, 255, 0, 0, 0, "TransitOnce", 1000)
misty.RegisterEvent(event_name='object_detection_event', event_type=Events.ObjectDetection, callback_function=recognized, keep_alive=False)
misty.KeepAlive()
