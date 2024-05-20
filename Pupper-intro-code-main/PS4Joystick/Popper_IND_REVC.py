from UDPComms import Publisher
import time


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

class RobotController:
    def __init__(self, port=8830, message_rate=20):
        self.drive_pub = Publisher(port)
        self.message_rate = message_rate
        self.default_command = {
            "L1": 0, "R1": 0, "x": 0, "circle": 0, "triangle": 0,
            "L2": 0, "R2": 0, "ly": 0, "lx": 0, "rx": 0,
            "message_rate": self.message_rate, "ry": 0, "dpady": 0, "dpadx": 0
        }

    # Commands
    def send_command(self, updates):
        command = self.default_command.copy()
        command.update(updates)
        print(command)
        try:
            self.drive_pub.send(command)
        except Exception as e:
            print("Failed to send command: {e}")

    def activate(self):
        self.send_command({"L1": 1})

    def trot(self):
        self.send_command({"R1": 0.2})

    def stop(self):
        self.send_command({})  # Send default command

    def move_forward(self, speed=0.5):
        self.send_command({"ly": speed})

    def move_left(self, speed=-0.2):
        self.send_command({"lx": speed})

    def move_right(self, speed=0.2):
        self.send_command({"lx": speed})

    def move_backwards(self, speed=-0.2):
        self.send_command({"ly": speed})

    def act_deactivate(self):
        self.send_command({"L1": 0})

    def pitch(self, pitch_value):
        self.send_command({"rx": pitch_value})

    def run_for_duration(self, action, duration, speed=0.2):
        start_time = time.time()
        while (time.time() - start_time) * 1000 < duration * 1000:  # Convert to msec
            action(speed)
            time.sleep(0.1)


# Main Execution

if __name__ == "__main__":
    controller = RobotController()
    controller.activate()
    time.sleep(1)
    controller.trot()
    time.sleep(1)

    controller.run_for_duration(controller.move_forward, 2, 0.4)    # Forward Control
    controller.run_for_duration(controller.pitch, 2, 0.2)    # Pitch Control

    # controller.stop()
    # time.sleep(2)
    controller.trot()
    time.sleep(1)

    controller.run_for_duration(controller.move_left, 5, 0.2)

    # controller.stop()
    # time.sleep(2)
    controller.trot()
    time.sleep(1)

    controller.run_for_duration(controller.move_backwards, 5, -0.2)

    controller.run_for_duration(controller.pitch, 3, 0.2)

    controller.act_deactivate()
