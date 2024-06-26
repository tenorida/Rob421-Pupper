from UDPComms import Publisher
import time

# drive_pub = Publisher(8830)
class DanceMoveCommands:

    def __init__(self):
        self.drive_pub = Publisher(8830) 
        
    def ActDeactivate(self):
        print("I am working")
        self.drive_pub.send({"L1": 1, 
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
    
    def trot(self):
        self.drive_pub.send({"L1": 0, 
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
    
    def move_forward(x):
        drive_pub.send({"L1": 0, 
                "R1": 0, 
                "x": 0, 
                "circle": 0, 
                "triangle": 0, 
                "L2": 0, 
                "R2": 0, 
                "ly": x, 
                "lx": 0, 
                "rx": 0, 
                "message_rate": 20, 
                "ry": 0, 
                "dpady": 0, 
                "dpadx": 0})
        
    def move_left():
        drive_pub.send({"L1": 0, 
                "R1": 0, 
                "x": 0, 
                "circle": 0, 
                "triangle": 0, 
                "L2": 0, 
                "R2": 0, 
                "ly": 0, 
                "lx": -1, 
                "rx": 0, 
                "message_rate": 20, 
                "ry": 0, 
                "dpady": 0, 
                "dpadx": 0})
    
    def move_right():
        drive_pub.send({"L1": 0, 
                "R1": 0, 
                "x": 0, 
                "circle": 0, 
                "triangle": 0, 
                "L2": 0, 
                "R2": 0, 
                "ly": 0, 
                "lx": 1, 
                "rx": 0, 
                "message_rate": 20, 
                "ry": 0, 
                "dpady": 0, 
                "dpadx": 0})
    
    def move_backwards():
        drive_pub.send({"L1": 0, 
                "R1": 0, 
                "x": 0, 
                "circle": 0, 
                "triangle": 0, 
                "L2": 0, 
                "R2": 0, 
                "ly": -1, 
                "lx": 1, 
                "rx": 0, 
                "message_rate": 20, 
                "ry": 0, 
                "dpady": 0, 
                "dpadx": 0})

# if __name__ == "__main__":
    # DanceMoveCommands.ActDeactivate()
    # time.sleep(1)
    # DanceMoveCommands.trot()
#     print("start trot")
#     time.sleep(1)
#     t0 = time.time()
#     diff = (time.time() - t0)
#     print (t0 * pow(10,3))
#     print(diff* pow(10,3))
#     print("moving foward")
#     while diff < 10000:
#         DanceMoveCommands.move_forward(0.4)
#         time.sleep(0.1)
#         #print("adjusting")
#         #move_left()
#         #time.sleep(5)
#         diff = (time.time() - t0) * pow(10,3) # msec
#         #print(diff)
#     DanceMoveCommands.ActDeactivate()
#     print("done")
