# Import necessary libraries
from PIL import Image
from typing import Generator

import numpy as np
import json
import cv2
import os

from source.MediaPipe.Face_Detection import face_detection


def crop_and_save(username, frame, coordinate, path, num_images, count=[0]):
    # x, y, w, h = coordinate
    # cropped_frame = frame[y:y + h, x:x + w]
    # image = Image.fromarray(cropped_frame)
    image = Image.fromarray(frame)

    if count[0] == 0:
        image.save(path + "/{}.jpg".format(username))

    if not os.path.exists(path + "/../Users/{0}".format(username)):
        os.makedirs(path + "/../Users/{0}".format(username))
    image.save(path + "/../Users/{0}/{0}_{1:02d}.jpg".format(username, count[0]))

    count[0] += 1
    if count[0] >= num_images:
        count[0] = 0
        return False
    else:
        return True


def is_blur(image, threshold=100):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the Laplacian of the image
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Return True if the variance is less than the threshold
    return laplacian_var < threshold


def validFace(frame, coordinate):
    x, y, w, h = coordinate
    frame_height, frame_width, _ = frame.shape

    # Face are not in the current frame
    if not (x >= 0 and y >= 0 and x + w <= frame_width and y + h <= frame_height):
        print("Face is not in the current frame")
        return False

    if is_blur(frame, threshold=300):
        print("Image is too blurry")
        return False

    target_area = 0.15 * frame_width * frame_height
    current_area = w * h

    if current_area < target_area:
        print("Face is too small")
        return False
    return True


def save_face_landmarks_list_to_file(username, landmarksList, path):
    np_data = np.array(landmarksList)
    np.save(path + "/{}.npy".format(username), np_data)


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
    if not os.path.exists("Data/Images"):
        os.makedirs("Data/Images")

    landmarks_list = []
    standardized_landmarks_list = []
    normalized_landmarks_list = []

    while webcam.isOpened() and flag:
        successful_frame_read, frame = webcam.read()
        if successful_frame_read:
            frame = cv2.flip(frame, 1)
            face_coordinates, landmarks, standardized_landmarks, normalized_landmarks = face_detection.detection(frame)

            if len(face_coordinates) == 1:
                coordinate = face_coordinates[0]
                x, y, w, h = coordinate

                # Take the face image when the face is in the window and big enough
                if validFace(frame, coordinate):
                    flag = crop_and_save(name, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), coordinate, "Data/Images", 100)

                    landmarks_list.append(landmarks[0])
                    standardized_landmarks_list.append(standardized_landmarks[0])
                    normalized_landmarks_list.append(normalized_landmarks[0])

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    dictionary["stopped"] = True
    json_object = json.dumps(dictionary)
    with open(os.path.join(__location__, "../../../static/json/streaming_data.json"), "w") as outfile:
        outfile.write(json_object)

    # Save the landmarks to files
    save_face_landmarks_list_to_file(name, landmarks_list, "Data/Landmarks/Original")
    save_face_landmarks_list_to_file(name, standardized_landmarks_list, "Data/Landmarks/Standardized")
    save_face_landmarks_list_to_file(name, normalized_landmarks_list, "Data/Landmarks/Normalized")

    # Release the webcam
    webcam.release()
    cv2.destroyAllWindows()
    print("Stop streaming...")
