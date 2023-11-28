import mediapipe as mp
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
import pickle
import time
from gestures import *

mp_hands = mp.solutions.hands
classes = ("down", "up", "stop", "thumbright", "thumbleft")

class HandNetwork(nn.Module):
    def __init__(self):
        super(HandNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(42, 120)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(120, 100)
        self.fc3 = nn.Linear(100, len(classes))
    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

with open("models/model6.pkl", "rb") as file:
    model = pickle.load(file)

pyautogui.PAUSE = 0
model.eval()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
frame_counter = 0
prev_time = 0
patience = 0
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        ret, image = cap.read()
        frame_counter += 1
        landmarks = []

        # Detections
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # changes from bgr to rgb since cv2 is bgr but mediapipe requires rgb
        image.flags.writeable = False
        results = hands.process(image) # this makes the actual detections
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if frame_counter % 3 == 0:
            if results.multi_hand_landmarks:
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
                for landmark in results.multi_hand_landmarks[0].landmark:
                    x, y = landmark.x, landmark.y
                    landmarks.append([x,y])
                with torch.no_grad():
                    landmarks = torch.tensor(landmarks)
                    out = model(landmarks.view(-1,21,2))
                    confidence = torch.max(F.softmax(out,1)).item()
                    prediction = torch.argmax(out)
                    print(classes[prediction], confidence)
                    if confidence >= 0.93:
                        if classes[prediction] == 'up':
                            increase_volume()
                        if classes[prediction] == 'down':
                            decrease_volume()
                        if classes[prediction] == 'stop':
                            play_pause()
                        if classes[prediction] == 'thumbright':
                            skip_track()
                        if classes[prediction] == 'thumbleft':
                            prev_track()
            else: # if hand is not detected for a set amt of frames, downscale to save pwr
                patience += 1
                if patience%30 == 0:
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
                    patience = 0

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