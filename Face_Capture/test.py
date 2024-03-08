# Import necessary libraries
import cv2
import sys

sys.path.append('../')
from Face_Detection import face_detection

#TODO: Connect to a camera to capture videos
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    successful_frame_read, frame = webcam.read()
    face_coordinates = face_detection.detection(frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)
    
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    # key is -1, no key has been pressed
    if key != -1:
        break

# Release the webcam
webcam.release()
cv2.destroyAllWindows()
