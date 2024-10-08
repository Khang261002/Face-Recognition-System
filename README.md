# Face-Recognition-System

This project implements a basic face recognition system using Haar cascades for face detection and face capture functionalities.

## Overview

The project consists of two main Python scripts:

1. `face_detection.py`: This script detects faces in a given image using the Haar cascade classifier. It loads the pre-trained model `haarcascade_frontalface_default.xml` and returns the coordinates of detected faces.

2. `face_capture.py`: This script captures video from the webcam, detects faces using the `face_detection` module, and crops the faces. It saves the cropped faces as individual images.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Khang261002/Face-Recognition-System.git
    ```

2. Install the required dependencies: (We are using Python 3.11)

    ```bash
    pip install opencv-python pillow numpy flask mediapipe face-recognition 
    ```

3. Run the `face_capture.py` script to start the face recognition system:

    ```bash
    python face_capture.py
    ```
4. Install dlib
    Download [dlib](https://github.com/Silufer/dlib-python/blob/main/dlib-19.24.1-cp311-cp311-win_amd64.whl)
    ```bash
    pip install /path/to/dlib-19.24.1-cp311-cp311-win_amd64.whl
    ```

5. Press any key to exit the program.

## File Structure

```bash
Face-Recognition-System
├── GUI
│ ├── templates
│ │ ├── Pictures
│ │ │ ├── kai.png
│ │ │ ├── khang.png
│ │ │ ├── wei.png
│ │ │ └── yu.png
│ │ ├── about.html
│ │ ├── checkin.html
│ │ ├── index.html
│ │ ├── register.html
│ │ └── styles.css
│ └── app.py
├── Haarcascade
│ ├── Face_Capture
│ │ ├── __init__.py
│ │ └── face_capture.py
│ ├── Face_Detection
│ │ ├── __init__.py
│ │ ├── face_detection.py
│ │ ├── haarcascade_eye.xml
│ │ └── haarcascade_frontalface_default.xml
│ └── Data
│   ├── user_0
│   │ ├── face_0.jpeg
│   │ ├── face_1.jpeg
│   │ └── ...
│   ├── user_1
│   │ ├── face_0.jpeg
│   │ ├── face_1.jpeg
│   │ └── ...
│   └── ...
├── MediaPipe
│ ├── Face_Capture
│ │ ├── __init__.py
│ │ └── face_capture.py
│ ├── Face_Detection
│ │ ├── __init__.py
│ │ └── face_detection.py
│ └── Data
│   ├── user_0
│   │ ├── face_0.jpeg
│   │ ├── face_1.jpeg
│   │ └── ...
│   ├── user_1
│   │ ├── face_0.jpeg
│   │ ├── face_1.jpeg
│   │ └── ...
│   └── ...
└── README.md
```

## Dependencies

- OpenCV (cv2)
- Pillow (PIL)
- NumPy

## Credits

This project was developed by Khang Duong, Yu Qing Leong, Kai Chun Goh, Wei Jin Gnoh.
