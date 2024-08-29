import face_recognition
import numpy as np
import dlib
import cv2

from source.FaceRecognition.Face_Encoding import face_encoding

def best_match_face(face_encodings, known_face_encodings, known_face_names):
    face_names = []
    for encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, encoding, tolerance=0.45)
        name = "Unknown"

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
    return face_names

def recognize():
    all_face_encodings = face_encoding.encode_new_faces()

    # Create arrays of known face encodings and their names
    known_face_encodings = np.array(list(all_face_encodings.values()))
    known_face_names = list(all_face_encodings.keys())

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    use_GPU = dlib.DLIB_USE_CUDA
    if use_GPU:
        print("Using GPU for face recognition")
    else:
        print("Using CPU for face recognition")

    webcam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    while webcam.isOpened():
        # Grab a single frame of video
        successful_frame_read, frame = webcam.read()
        if successful_frame_read:
            frame = cv2.flip(frame, 1)

            # Resize frame of video to 1/4 size for faster face recognition processing
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            if not use_GPU:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            else:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_frame)
                # Re-sample the face for more precise recognition
                if use_GPU:
                    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations, 50, model="large")
                else:
                    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations, model="large")

                face_names = best_match_face(face_encodings, known_face_encodings, known_face_names)

            # Process less frames only for higher fps
            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                if not use_GPU:
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

                # Draw a label with a name below the face
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left, bottom + 25), font, 1, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release handle to the webcam
    webcam.release()
    cv2.destroyAllWindows()
    print("Stop streaming...")
