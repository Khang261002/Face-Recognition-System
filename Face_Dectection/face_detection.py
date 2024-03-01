# Import necessary libraries
import cv2

#TODO: Load the trained model "haarcascade_frontalface_default.xml" in the Model folder
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#TODO: Connect to a camera to capture videos
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#TODO: Make a loop to continuously capture frames from the camera
#TODO: Use the trained model to get the coordinates of the faces
#TODO: Draw a rectangle around faces that are detected and show the camera video
#TODO: Use waitKey() to exit the loop
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    if key != -1:
        break

# Release the webcam
webcam.release()
cv2.destroyAllWindows()
