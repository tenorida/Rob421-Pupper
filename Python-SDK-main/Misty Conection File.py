#Misty conection
from mistyPy.Robot import Robot

def start_skill():
    current_response = misty.move_arms(50, 150)
    print(current_response)
    print(current_response.status_code)
    print(current_response.json())
    print(current_response.json()["result"])

if __name__ == "__main__":
    ipAddress = "192.168.0.102"
    misty = Robot(ipAddress)
    start_skill()
