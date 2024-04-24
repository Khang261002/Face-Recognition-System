import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
while webcam.isOpened():
    successful_frame_read, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Applying face mesh model using MediaPipe
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame)

    # Draw annotations on the image
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
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
                    
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 255), 2)

            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style()
            )

            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style()
            )

    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    if key != -1:
        break

# Release the webcam
webcam.release()
cv2.destroyAllWindows()
