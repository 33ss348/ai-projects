import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolum
from cometypes import CLSCTX_ALL
from math import hypot
import screenbrightnesscontrol as sbc
mp_hands=mp.solution.hands
hands =mp_hands.Hands(min_detection_confidence=0.7)