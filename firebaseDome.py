
import pyrebase

config = {
    "apiKey": "AIzaSyCtGBHOtz8XIu6PsmrAXKfvurW6FsW_Vpk",
    "authDomain": "mediapipev1.firebaseapp.com",
    "databaseURL": "https://mediapipev1-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "mediapipev1.appspot.com"
}
firebase = pyrebase.initialize_app(config)

firebase.database()
db = firebase.database()

db.child("value").update({"val": "0"})
