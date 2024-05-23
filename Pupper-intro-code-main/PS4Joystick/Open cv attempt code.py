#Python Pupper Saultz_Tristan Individual Artifact#
import cv2 as cv
import time


# Open the default camera 
cap = cv.VideoCapture(0, cv.CAP_V4L)

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv.imshow('Webcam', frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

