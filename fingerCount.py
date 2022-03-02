import cv2
import mediapipe as mp

import pyrebase

import time

firebaseConfig = {
  'apiKey': "*****************-*****************",
  'authDomain': "*****************.firebaseapp.com",
  'databaseURL': "**************************************",
  'projectId': "*****************",
  'storageBucket': "*****************.appspot.com",
  'messagingSenderId': "*****************",
  'appId': "1:*****************:web:*****************",
  'measurementId': "*****************-*****************"
}


config = {
    "apiKey": "*****************-*****************",
    "authDomain": "*****************.firebaseapp.com",
    "databaseURL": "https://*****************-*****************-*****************.*****************.com",
    "storageBucket": "*****************.*****************.com"
}
firebase = pyrebase.initialize_app(firebaseConfig)

firebase.database()
db = firebase.database()

# db.child("value").update({"val": "0"})


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

val = 0

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=1,
        min_detection_confidence=0.85,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        # image = cv2.flip(image, 1)
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y  # x ve y koordinatlarini alindi
                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y

                font = cv2.FONT_HERSHEY_PLAIN

                if y1 > y:
                    cv2.putText(image, text='KAPALI', org=(100, 100), fontScale=font, fontFace=4, color=(255, 255, 0),
                                thickness=3)
                    val = '0'
                    if val == '0':
                        # db.child("value").update({"val": val})
                        db.update({"val": val})
                        #time.sleep(0.1)





                else:
                    cv2.putText(image, text='ACIK', org=(100, 100), fontScale=font, fontFace=4, color=(255, 255, 0),
                                thickness=3)
                    val = '1'
                    if val == '1':
                        # db.child("value").update({"val": val})
                        db.update({"val": val})
                        #time.sleep(0.1)

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
