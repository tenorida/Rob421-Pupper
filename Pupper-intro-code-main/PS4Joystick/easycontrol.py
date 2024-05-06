from UDPComms import Publisher
import time 

# drive_pub = Publisher(8830) = controls movement of pupper (basically mode 1)
# arm_pub = Publisher(8410) = controls more movements of upper (mode 2)
# mode 2 is what you can do when pupper is not in trot mode when using a controller.
drive_pub = Publisher(8830) 
# arm_pub = Publisher(8410)
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
    
# TODO: create functions that allow the robot to move around (forward,back,right,left,....)
# Remember: The inputs are mainly digital except for the lx,ly and rx,ry controls.
# The digital inputs do not reset after being call unless you design them to! (i.e., if you press L1 it will remaind press)
# Each action needs to be press once then can be ignored (you don't have to keep L1 as 1 you can create an activate function the forget about it)   
# TODO: make the robot move through the racing track
if __name__ == "__main__":
    activate()
    