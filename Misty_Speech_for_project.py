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