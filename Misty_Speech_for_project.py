#Speech for Misty
#What will Misty interact with? I am thinking backpacks, humans, and chairs. I cannot think of anything else at the moment, but feel free to add other things to it.

import sounddevice
from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time
from scipy.io.wavfile import write
import whisper
model = whisper.load_model("base")

ipAddress = "192.168.0.XXX"
misty = Robot(ipAddress)



def Key_Phrase_Recognized(data): #Wake up misty with key phrase
    print(data)
    misty.DisplayImage("e_Surprise.jpg", 1)
    misty.PlayAudio("s_PhraseHello.wav", 30)
    time.sleep(2)
    misty.Speak("Good morning")
    misty.MoveHead(0, 0, 0, 80)
    misty.MoveArms(-85, -85, 80, 80)
    time.sleep(2)
    
#if chair - pushes it?








#if human - speaks





#if backpack - "whose shit is this? Get it out of here!"






#if other object.......
