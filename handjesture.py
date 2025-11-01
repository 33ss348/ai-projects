import cv2 ,time,pyautogui
import mediapipe as mp
mphands=mp.solutions.hands
hands=mphands.Hands(maxnumberhands=1,meandetectionconfedens=0.7)
mp.solutions.drawing_utils
scrollspeed=300
scroll_delay=1
camwith,camhight=640,480 
def detectjesture(landmarks,handedness):
    fingers=[] 
    teps=(mphands.handlandmarks.index_finger_tip,mphands.handlandmarks.middle_finger_tip)