# Import necessary libraries
from PIL import Image
import cv2
import sys

sys.path.append('../')
from Face_Detection import face_detection

#TODO: Crop the image using the coordinate provided and save it
def crop_and_save(frame, coordinate, path, num_images, count=[0]):
    x, y, w, h = coordinate
    cropped_frame = frame[y:y + h, x:x + w]
    im = Image.fromarray(cropped_frame)
    im.save(path + "img_{}.jpeg".format(count[0]))
    
    count[0] += 1
    if count[0] == num_images:
        return False
    else:
        return True

#TODO: Connect to a camera to capture videos
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
flag = True

while flag:
    successful_frame_read, frame = webcam.read()
    face_coordinates = face_detection.detection(frame)

    for coordinate in face_coordinates:
        x, y, w, h = coordinate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)
        flag = crop_and_save(frame, coordinate, "./Data/", 100)
    
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    # key is -1, no key has been pressed
    if key != -1:
        break

# Release the webcam
webcam.release()
cv2.destroyAllWindows()
