from UDPComms import Publisher
import time

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
        try:
            self.drive_pub.send(command)
        except Exception as e:
            print(f"Failed to send command: {e}")

    def activate(self):
        self.send_command({"L1": 1})

    def trot(self):
        self.send_command({"R1": 1})

    def stop(self):
        self.send_command({})  # Send default command

    def move_forward(self):
        self.send_command({"ly": 1})

    def move_left(self):
        self.send_command({"lx": -1})

    def move_right(self):
        self.send_command({"lx": 1})

    def move_backwards(self):
        self.send_command({"ly": -1})


# Main Execution

if __name__ == "__main__":
    controller = RobotController()
    controller.activate()
    time.sleep(1)
    for _ in range(4):
        controller.move_forward()
        time.sleep(1)
        controller.move_left()
        time.sleep(1)
        controller.move_backwards()
        time.sleep(1)
        controller.move_left()
    controller.stop()
