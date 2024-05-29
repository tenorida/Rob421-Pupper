import sys, os
import cv2
import numpy as np
from time import sleep
from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

ROBOT_IP = "192.168.0.102"
FOLLOW_DISTANCE = 0.5  # distance [m] to follow the human
FOLLOW_THRESHOLD = 0.1  # acceptable threshold distance

misty_robot = Robot(ROBOT_IP)

# Load YOLO object detection model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
classes = open("coco.names").read().strip().split("\n")
human_class_index = classes.index("person")

following_human = False


def stop_robot():
    misty_robot.stop()


def follow_human(distance):
    if distance > FOLLOW_DISTANCE + FOLLOW_THRESHOLD:
        # Move forward
        linear_velocity = 30
    elif distance < FOLLOW_DISTANCE - FOLLOW_THRESHOLD:
        # Move backward
        linear_velocity = -30
    else:
        # Stop if within the acceptable threshold
        linear_velocity = 0

    misty_robot.drive_time(linear_velocity=linear_velocity, angular_velocity=0, time_ms=500)


def tof_callback(message):
    global following_human
    distance = message["message"]["distanceInMeters"]
    sensor_id = message["message"]["sensorId"]

    # Use front-center ToF sensor to maintain distance to the human
    if sensor_id == "frontcenter":
        if following_human:
            follow_human(distance)


def detect_human(image):
    global following_human
    height, width, channels = image.shape
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if class_id == human_class_index and confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    if len(indexes) > 0:
        following_human = True
        for i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, label, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    return image


if __name__ == "__main__":
    try:
        # Subscribe to the front ToF sensors
        front_right = misty_robot.register_event(
            Events.TimeOfFlight, "frontright", condition=[EventFilters.TimeOfFlightPosition.FrontRight],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )
        front_center = misty_robot.register_event(
            Events.TimeOfFlight, "frontcenter", condition=[EventFilters.TimeOfFlightPosition.FrontCenter],
            keep_alive=True, callback_function=tof_callback, debounce=0
        )
        front_left = misty_robot.register_event(
            Events.TimeOfFlight, "frontleft", condition=[EventFilters.TimeOfFlightPosition.FrontLeft], keep_alive=True,
            callback_function=tof_callback, debounce=0
        )

        # Subscribe to the back ToF sensors (for additional obstacle detection)
        # back_right = misty_robot.register_event(
        #     Events.TimeOfFlight, "backright", condition=[EventFilters.TimeOfFlightPosition.BackRight], keep_alive=True,
        #     callback_function=tof_callback, debounce=0
        # )
        back_center = misty_robot.register_event(
            Events.TimeOfFlight, "backcenter", condition=[EventFilters.TimeOfFlightPosition.Back], keep_alive=True,
            callback_function=tof_callback, debounce=0
        )
        # back_left = misty_robot.register_event(
        #     Events.TimeOfFlight, "backleft", condition=[EventFilters.TimeOfFlightPosition.BackLeft], keep_alive=True,
        #     callback_function=tof_callback, debounce=0
        # )

        # Capture images and detect humans
        while True:
            image_response = misty_robot.take_picture()
            if image_response.status == "Success":
                image_uri = image_response.result["imageUri"]
                image_data = misty_robot.download_image(image_uri)
                nparr = np.frombuffer(image_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                img = detect_human(img)
                cv2.imshow("Human Detection", img)
                cv2.waitKey(1)

        # Using the keep_alive() function to keep the main thread alive
        misty_robot.keep_alive()

    except Exception as ex:
        print(ex)
    finally:

        misty_robot.unregister_all_events()
