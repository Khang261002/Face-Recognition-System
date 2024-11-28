"""
Face Detection and Landmark Extraction using Mediapipe and OpenCV.

This module provides a function `detection` that processes video frames to 
detect facial landmarks using Mediapipe's Face Mesh solution. The function 
returns bounding box coordinates for the face and 3D landmark positions.

Dependencies:
- OpenCV (cv2)
- Mediapipe
- NumPy
"""
from typing import List, Tuple, Union
import mediapipe as mp
import cv2
import numpy as np

from source.MediaPipe.Face_Detection.landmarks_normalization import normalize_landmarks

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)


def standardize_landmarks(landmarks, x, y, w, h, W, H):
    for landmark in landmarks:
        landmark[0] = (landmark[0]*W - x) / w
        landmark[1] = (landmark[1]*H - y) / h
    return landmarks


def detection(frame: np.ndarray) -> \
        Union[
            Tuple[List[Tuple[int, int, int, int]], List[List[float]]],
            Tuple[List[None], List[None]]
        ]:
    """
    Detects face landmarks and returns face coordinates and landmarks.

    Args:
        frame (np.ndarray): Input video frame as a NumPy array.

    Returns:
        Union[Tuple[List[Tuple[int, int, int, int]], List[List[float]]], 
              Tuple[List[None], List[None]]]:
        - Tuple containing face coordinates (bounding boxes) 
          and face landmarks (x, y, z).
        - If no landmarks are detected, returns empty lists.
    """
    H, W, c = frame.shape

    # Applying face mesh model using MediaPipe
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame)

    # Getting the coordinates of the face
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    face_coordinates = []
    landmarks_list = []
    standardized_landmarks_list = []
    normalized_landmarks_list = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            x_max = 0
            y_max = 0
            x_min = W
            y_min = H
            landmarks = []
            
            for landmark in face_landmarks.landmark:
                x, y = int(landmark.x * W), int(landmark.y * H)
                landmarks.append([landmark.x, landmark.y, landmark.z])
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y

            # Return value as form (x, y, w, h)
            face_coordinates.append(
                (x_min, y_min, x_max - x_min, y_max - y_min)
            )
            landmarks_list.append(landmarks)
            standardized_landmarks_list.append(
                standardize_landmarks(
                    landmarks.copy(),
                    x_min, y_min,
                    x_max - x_min, y_max - y_min,
                    W, H
                )
            )
            normalized_landmarks_list.append(
                normalize_landmarks(
                    landmarks.copy(),
                    W, H
                )
            )

    return (face_coordinates, landmarks_list, standardized_landmarks_list, normalized_landmarks_list)
