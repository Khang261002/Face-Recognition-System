import cv2
import numpy as np
from PIL import Image
import os

import face_detection

# Path for face image database
path = 'Data\khang'
recognizer = cv2.face.LBPHFaceRecognizer_create()

# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]     
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        id = 1
        faces = face_detection.detection(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)
    return faceSamples, ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
# Save the model into trainer/trainer.yml
recognizer.write('Trainer/trainer.yml') 
# Print the number of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
