"""ONLY GNU+Linux is supported. MacOS may work, but Windows probably won't. 
This file contains the main loop, while the other file handles game logic."""

# setup
from sys import platform
import os
import time
if not platform == "linux":
    print(f"Please run on GNU+Linux instead of {platform}.")
    exit()
try:
    import keyboard
except ImportError:
    print("Please install the keyboard library. ")
    exit()
width = 3
height = 3
board = [" " for i in range(width*height)]
selected_location = 4

def draw_board(key):
    os.system("clear")
    

os.system("clear")

# main loop
while True:
    if keyboard.is_pressed("left"):
        selected_location -= 1
        draw_board()
    if keyboard.is_pressed("right"):
        selected_location += 1
        draw_board()
    if keyboard.is_pressed("up"):
        pass
    if keyboard.is_pressed("down"):
        pass
    time.sleep(0.1)