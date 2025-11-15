import numpy as np
import mediapipe as mp
import cv2
import time
mp_hands=mp.solutions.hands
hands=mp_hands.hands(min detection_confidence=0.7,min traking_confidence=0.7)
mpdraw=mp.solutions.drawing_utils
filters=[none,'sepia','grayscale','negative','blur']
currentfilter=0
cap=cv2.video_capture
if not cap.is_Opened():
    print("ERRO CLUDE NOT ACSSES THE WEB CAM")
    exit()