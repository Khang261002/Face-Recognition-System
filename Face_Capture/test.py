# Import necessary libraries
import cv2
import sys

sys.path.append('../')
from Face_Detection import face_detection

def crop_and_save(frame, coordinate, path):
    x, y, w, h = coordinate
    cropped_frame = frame[y:y + h, x:x + w]
    # cropped_frame.save(path)

#TODO: Connect to a camera to capture videos
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    successful_frame_read, frame = webcam.read()
    face_coordinates = face_detection.detection(frame)

    for coordinate in face_coordinates:
        x, y, w, h = coordinate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)
        crop_and_save(frame, coordinate, "")
    
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    # key is -1, no key has been pressed
    if key != -1:
        break

# Release the webcam
webcam.release()
cv2.destroyAllWindows()
