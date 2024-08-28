import face_recognition
import pickle
import os

def get_all_encodings(filepath):
    # Load face encodings if file exists, create if not.
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            print("Loading all face encodings...")
            all_face_encodings = pickle.load(f)
    else:
        print("Creating new file for all face encodings...")
        all_face_encodings = {}
    
    return all_face_encodings

def load_all_images(path):
    images_data = []

    for filename in os.listdir(path):
        images_data.append((filename.split('.')[0], face_recognition.load_image_file(os.path.join(path, filename))))

    return images_data

def encode_new_faces(filename="dataset_faces.pkl", update=False):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path_to_encodings = os.path.join(__location__, 'Data/Encodings/{}'.format(filename))
    path_to_images = os.path.join(__location__, 'Data/Images')
    all_face_encodings = get_all_encodings(path_to_encodings)
    
    # Add new or update existing face encodings
    for (username, image) in load_all_images(path_to_images):
        if (not update) and (username in all_face_encodings):
            print("{}'s face has already been encoded".format(username))
            continue
        else:
            all_face_encodings[username] = face_recognition.face_encodings(image)[0]

    with open(path_to_encodings, 'wb') as f:
        pickle.dump(all_face_encodings, f)
    
    return all_face_encodings
