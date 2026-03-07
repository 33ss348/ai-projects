import threading
import sys
try:
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wabe
import speechrecognisation as sr
from speechrecognisation import data
except ImportError as e :
print("missing library")
print("install comands")
sys.exit(1)
stop_event=threading.Event
def waitforenter():
input("press enter to stop recording")
stop_event.set()
def spinner():
    chars="i=0"
    while not stop_event.is_set()
    i=i+1
    time.sleep(0.1)