import cv2
import mediapipe as mp
import torch
import torch.nn.functional as F
from HandNetwork import HandNetwork
import time
from gestures import *

class Camera():
    def __init__(self, confidence_threshold=0.95):
        self.classes = ("down", "up", "stop", "thumbright", "thumbleft", "right", "left", "background")
        self.model = HandNetwork(classes=self.classes)
        self.model = torch.load("models/model8.pth")
        self.capture_session = cv2.VideoCapture(0)
        self.frame_counter = 0
        self.patience = 0
        self.low_power = 3
        self.confidence_threshold = confidence_threshold

    def start_capture_session(self):
        mp_hands = mp.solutions.hands
        prev_time = 0
        default_width =  int(self.capture_session.get(3))
        default_height = int(self.capture_session.get(4))
        self.capture_session.set(cv2.CAP_PROP_FRAME_WIDTH, int(default_width/3))
        self.capture_session.set(cv2.CAP_PROP_FRAME_HEIGHT, int(default_height/3))
        with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=2) as hands:
            while self.capture_session.isOpened():
                ret, image = self.capture_session.read()
                self.frame_counter += 1
                landmarks = []
                if self.frame_counter % self.low_power == 0:
                    # Detections
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # changes from bgr to rgb since cv2 is bgr but mediapipe requires rgb
                    image.flags.writeable = False
                    results = hands.process(image) # this makes the actual detections
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    if self.frame_counter % 3 == 0:
                        if results.multi_hand_landmarks:
                            self.capture_session.set(cv2.CAP_PROP_FRAME_WIDTH, default_width)
                            self.capture_session.set(cv2.CAP_PROP_FRAME_HEIGHT, default_height)
                            self.low_power = 1
                            for landmark in results.multi_hand_landmarks[0].landmark:
                                x, y = landmark.x, landmark.y
                                landmarks.append([x,y])
                            with torch.no_grad():
                                landmarks = torch.tensor(landmarks)
                                out = self.model(landmarks.view(-1,21,2))
                                confidence = torch.max(F.softmax(out,1)).item()
                                prediction = torch.argmax(out)
                                print(self.classes[prediction], confidence)
                                if confidence >= self.confidence_threshold:
                                    if self.classes[prediction] == 'up':
                                        increase_volume()
                                    if self.classes[prediction] == 'down':
                                        decrease_volume()
                                    if self.classes[prediction] == 'stop':
                                        play_pause()
                                    if self.classes[prediction] == 'thumbright':
                                        skip_track()
                                    if self.classes[prediction] == 'thumbleft':
                                        prev_track()
                                    if self.classes[prediction] == 'right':
                                        scrub_spotify(10)
                                    if self.classes[prediction] == 'left':
                                        scrub_spotify(-10)
                        else: # if hand is not detected for a set amt of frames, downscale to save pwr
                            self.patience += 1
                            if self.patience%15 == 0:
                                self.capture_session.set(cv2.CAP_PROP_FRAME_WIDTH, int(default_width/3))
                                self.capture_session.set(cv2.CAP_PROP_FRAME_HEIGHT, int(default_height/3))
                                self.patience = 0
                                self.low_power = 3

                # Print fps
                curr_time = time.time()
                fps = 1 / (curr_time-prev_time)
                prev_time = curr_time
                image = cv2.flip(image,1)
                cv2.putText(image, f"FPS: {fps}", (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)

                cv2.imshow("Hand Tracking", image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    self.end_capture_session()
                    break
            
    def end_capture_session(self):
        self.capture_session.release()
        cv2.destroyAllWindows()
