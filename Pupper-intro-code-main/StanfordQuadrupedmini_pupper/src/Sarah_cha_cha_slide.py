#Cha Cha Slide
# L1 = activate/disactivate
# R1 = transition between Rest mode and Trot mode.
# circle = dance or hold for 3 seconds to turn off system
# trinagle  = NOTHING 
# X = jump
# L2 = nothing
# R2 = Nothing
# The range for the following are form (-1, 1)
# ly = forward or backwards
# lx = left or right
# rx = turn left or right (pitch)
# ry = pitches the robot forward


from MovementGroup import MovementGroups
Move = MovementGroups()


from  leg_move import MoveServos
from  leg_move import MoveServos

from UDPComms import Publisher
import time

drive_pub = Publisher(8830)

def activate():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def trot():
    drive_pub.send({"L1": 0, 
            "R1": 1, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def stop():
    drive_pub.send({"L1": 0, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def move_foward():
    drive_pub.send({"L1": 0, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0.5, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
    
def move_left():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": -0.3, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def move_right():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0.3, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def move_backwards():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": -0.5, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def move_jumpdown():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": -1, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
def move_jumpup():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 1, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def move_chacha():
    Move.look_right()
    Move.look_upperright()
    Move.look_up()
    Move.look_upperleft()
    Move.look_left()
    Move.look_leftlower()
    Move.look_down()
    Move.look_rightlower()
    Move.look_right()
    Move.stop()
    Move.move_right()
    Move.move_forward()
    Move.move_left()
    Move.move_backward()
    Move.move_right()
    Move.stop()




if __name__ == "__main__":
    activate()
    time.sleep(1)
    for i in range(0,2):
        trot()
        time.sleep(1)
        #    to the left
    while True:
        print("move left")
        #move_left()
        #time.sleep(1)
        #    take it back now y'all
        #move_backwards()
        #time.sleep(1)
        #    one hop this time
        #move_jumpdown()
        #time.sleep(1)
        #move_jumpup()
        #time.sleep(1)
        #    one hop this time
        move_jumpdown()
        #time.sleep(1)
        #move_jumpup()
        #time.sleep(1)
        #    right foot two stomps
        #MoveServos.move_servo13()
        #time.sleep(1)
        #MoveServos.move_servo13()
        #time.sleep(1)
        #    left foot two stomps
        #MoveServos.move_servo10()
        #time.sleep(1)
        #MoveServos.move_servo10()
        #time.sleep(1)
        #    cha cha real smooth
        #move_chacha()
        print ("done")
    stop()
