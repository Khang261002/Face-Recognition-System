import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

def detection(frame):
    h, w, c = frame.shape

    # Applying face mesh model using MediaPipe
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame)

    # Getting the coordinates of the face
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    face_coordinates = []
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h

            for landmark in face_landmarks.landmark:
                x, y = int(landmark.x * w), int(landmark.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            # Return value as form (x, y, w, h)
            face_coordinates.append((x_min, y_min, x_max - x_min, y_max - y_min))
    
    return face_coordinates