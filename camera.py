import mediapipe as mp
import cv2
import torch
import torch.nn as nn
import pickle
import time
from gestures import *
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
classes = ("down", "up", "thumbs up")

class HandNetwork(nn.Module):
    def __init__(self):
        super(HandNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(42, 120)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(120, 100)
        self.fc3 = nn.Linear(100, 3)
    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

with open("models/model2.pkl", "rb") as file:
    model = pickle.load(file)

cap = cv2.VideoCapture(0)
frame_counter = 0
prev_time = 0
with mp_hands.Hands(min_detection_confidence=0.95, min_tracking_confidence=0.7, max_num_hands=1) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        landmarks = []
        # Detections
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # changes from bgr to rgb since cv2 is bgr but mediapipe requires rgb
        image.flags.writeable = False
        results = hands.process(image) # this makes the actual detections
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        frame_counter += 1

        if results.multi_hand_landmarks:
            for landmark in results.multi_hand_landmarks[0].landmark:
                x, y = landmark.x, landmark.y
                landmarks.append([x,y])
            landmarks = np.array(landmarks)
            out = model.predict(landmarks.reshape(-1,21*2)[0].reshape(1,-1)).item()
            print(f"Prediction: {classes[out]}")
            if classes[out] == 'up':
                increase_volume()
            if classes[out] == 'down':
                decrease_volume()
            if classes[out] == 'thumbs up':
                skip_track()

        # Print fps
        curr_time = time.time()
        fps = 1 / (curr_time-prev_time)
        prev_time = curr_time
        image = cv2.flip(image,1)
        cv2.putText(image, f"FPS: {fps}", (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)

        cv2.imshow("Hand Tracking", image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()