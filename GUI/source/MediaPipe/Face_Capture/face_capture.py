# Import necessary libraries
from PIL import Image
from typing import Generator

import json
import cv2
import os

from source.MediaPipe.Face_Detection import face_detection

def crop_and_save(username, frame, coordinate, path, num_images, count=[0]):
    x, y, w, h = coordinate
    cropped_frame = frame[y:y + h, x:x + w]
    im = Image.fromarray(cropped_frame)
    im.save(path + "/{}.jpg".format(username))

    count[0] += 1
    if count[0] >= num_images:
        count[0] = 0
        return False
    else:
        return True
    
def validFace(frame, coordinate):
    x, y, w, h = coordinate
    frame_height, frame_width, _ = frame.shape

    # Face are not in the current frame
    if not (x >= 0 and y >= 0 and x + w <= frame_width and y + h <= frame_height):
        return False

    target_area = 0.15 * frame_width * frame_height
    current_area = w * h

    if current_area < target_area:
        return False
    return True

def capture(name) -> Generator[bytes, None, None]:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    dictionary = {
        "stopped": False
    }
    json_object = json.dumps(dictionary)
    with open(os.path.join(__location__, "../../../static/json/streaming_data.json"), "w") as outfile:
        outfile.write(json_object)

    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)     # for Windows
    # webcam = cv2.VideoCapture(0)                    # for Other OSes
    flag = True
    if not os.path.exists("Data/{}".format(name)):
        os.makedirs("Data/{}".format(name))

    while webcam.isOpened() and flag:
        successful_frame_read, frame = webcam.read()
        if successful_frame_read:
            frame = cv2.flip(frame, 1)
            face_coordinates = face_detection.detection(frame)

            for coordinate in face_coordinates:
                x, y, w, h = coordinate

                # Take the face image when the face is in the window and big enough
                if validFace(frame, coordinate):
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    flag = crop_and_save(name, gray, coordinate, "Data/Images/", 1)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    dictionary["stopped"] = True
    json_object = json.dumps(dictionary)
    with open(os.path.join(__location__, "../../../static/json/streaming_data.json"), "w") as outfile:
        outfile.write(json_object)

    # Release the webcam
    webcam.release()
    cv2.destroyAllWindows()
    print("Stop streaming...")
