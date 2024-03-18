# Import necessary libraries
import numpy as np
import cv2

#TODO: Load the trained model "haarcascade_frontalface_default.xml" in the Model folder
trained_face_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detection(frame) -> tuple | np.ndarray | None:
    #TODO: Use the trained model to get the coordinates of the faces
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_model.detectMultiScale(
        grayscaled_frame,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # print(type(face_coordinates))

    return face_coordinates
