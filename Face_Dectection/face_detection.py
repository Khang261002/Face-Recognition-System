# Import necessary libraries
import cv2

#TODO: Load the trained model "haarcascade_frontalface_default.xml" in the Model folder
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#TODO: Connect to a camera to capture videos
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#TODO: Make a loop to continuously capture frames from the camera
#TODO: Use the trained model to get the coordinates of the faces

#TODO: Draw a rectangle around faces that are detected
#TODO: Use waitKey() to exit the loop
