# Import necessary libraries
from PIL import Image
from typing import Generator

import cv2
import sys
import os

from source.MediaPipe.Face_Detection import face_detection

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

def capture(name) -> Generator[bytes, None, None]:
    webcam = cv2.VideoCapture(0)
    flag = True
    if not os.path.exists("Data/{}".format(name)):
        os.makedirs("Data/{}".format(name))

    while webcam.isOpened() and flag:
        successful_frame_read, frame = webcam.read()
        face_coordinates = face_detection.detection(frame)

        for coordinate in face_coordinates:
            x, y, w, h = coordinate
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)

            # # Add if statement to avoid saving the face that is not fully shown
            # if (x >= 0 and y >= 0 and x + w <= frame.shape[0] and y + h <= frame.shape[1]):
            #     flag = crop_and_save(frame, coordinate, "Data/{}".format(name), 100)
        
        # cv2.imshow('Face Detector', frame)
        # key = cv2.waitKey(1)
        # # key is -1, no key has been pressed
        # if key != -1:
        #     break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the webcam
    webcam.release()
    cv2.destroyAllWindows()
