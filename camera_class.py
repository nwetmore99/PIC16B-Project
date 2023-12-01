import cv2
import mediapipe as mp
import torch
import torch.nn.functional as F
from HandNetwork import HandNetwork

class Camera():
    def __init__(self):
        self.classes = ("down", "up", "stop", "thumbright", "thumbleft")
        self.model = HandNetwork(classes=("down", "up", "stop", "thumbright", "thumbleft"))
        self.model = torch.load("models/model.pth")
        self.capture_session = cv2.VideoCapture(0)
        self.capture_session.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture_session.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
        self.frame_counter = 0
        self.patience = 0
