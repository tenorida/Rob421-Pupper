#Misty Python Artifact Assign.

import sounddevice
from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time
from scipy.io.wavfile import write
import whisper
model = whisper.load_model("base")

ipAddress = "192.168.0.103"
misty = Robot(ipAddress)


#goal: build on previous artifact, add movement

def Key_Phrase_Recognized(data): #Wake up misty with key phrase
    print(data)
    misty.DisplayImage("e_Surprise.jpg", 1)
    misty.PlayAudio("s_PhraseHello.wav", 30)
    time.sleep(2)
    misty.Speak("Good morning")
    misty.MoveHead(0, 0, 0, 80)
    misty.MoveArms(-85, -85, 80, 80)
    time.sleep(2)
    StartConvo()

    def StartConvo():
        for i in range(0,4):
            misty.Speak("Wow that was a tough maze. Would you rather go through the maze or listen to Polish music?")
            time.sleep(1)
            S = RecordAudio()
            responce = TranscribeAudio(S)

            if "Polish Music" in responce.lower():
                time.sleep(2)
                HandleMusic()
            
            elif "Maze" in responce.lower():
                time.sleep(2)
                HandleMaze()
            
            else:
                TryAgain(i)


def RecordAudio(): #Function to record sound
    print('Recording audio now.')
    my_recording = sounddevice.rec(int(seconds*f_s), f_s, 2)
    sounddevice.wait()
    write('output.wav', f_s, my_recording)
    return "output.wav"

def TranscribeAudio(Sp): #Function to return audio in text format
    print('Transcribing audio.')
    result = model.transcribe(Sp, fp16=False)
    print(f"What was heard: {result['text']}")
    return result["text"]

def TryAgain(k):
    if k==3:
        misty.Speak("Too many tries, I will go to sleep now")
        exit() #ends the program
    misty.Speak("Did not hear right")
    time.sleep(3)

#Classical option
def HandleMusic():
    for k in range(0,4):
        misty.Speak("Okay, here is some Polish Music!")
        time.sleep(1)
        misty.PlayAudio(pl)
        misty.DisplayImage()

        for i in range(5):
            misty.MoveArms(70, -50) 
            time.sleep(0.3) 
            misty.MoveArms(70, 0)
            time.sleep(0.3)

        exit()

#Shanties opition
def HandleMaze():
    for k in range(0,4):
        misty.Speak("Okay, lets go back through the maze! ")

        exit()


misty.RegisterEvent(event_name='Key_Phrase_Recognized', event_type=Events.KeyPhraseRecognized, callback_function=Key_Phrase_Recognized, keep_alive=True)
misty.StartKeyPhraseRecognition()
print("Ready to start")          
misty.KeepAlive()