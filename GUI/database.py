import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("GUI/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-recognition-system-1f089-default-rtdb.firebaseio.com/"
})

ref = db.reference('users')

data = {
    "312654":
    {
        "name":"Wei Jin",
        "major":"Computer Science"
    },
    "312655":
    {
        "name":"Khang Duong",
        "major":"Computer Science"
    },
}

for key,value in data.items():
    ref.child(key).set(value)