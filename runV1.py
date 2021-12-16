print("Autodrawer v1 (JPG images only)")

from PIL import Image
import time

import pyautogui
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

import os
import math
import keyboard


def getImageLink():
    cwd = os.path.dirname(os.path.abspath(__file__))
    img_link = os.path.join(cwd, "img\\trooper.jpg")
    return img_link

myImg = Image.open(getImageLink())
pix = myImg.load()
width,height = myImg.size

draw_parems = {
    "gap": float(input("gap:")),
    "top_x": pyautogui.position().x,
    "top_y": pyautogui.position().y
}

color_0 = (0,0,0)
color_1 = (64,64,64)
color_2 = (128,128,128)

def scanImage():
    interactions = 0
    for y in range(0, height, 1):
        print(f"running.. {math.trunc(y/height * 100)}% ")
        for x in range(0,width,1):

            # CUSTOM FAIL SAFE BUTTON
            if keyboard.is_pressed("esc"):
                time.sleep(1)
                break

            if pix[x,y] >= color_0 and pix[x,y] <= color_2:
                clickCanvas(x,y, draw_parems)
                interactions += 1
        os.system('cls||clear')

    print("Completed!")
    return interactions

def clickCanvas(x,y,obj):
    top_x = obj["top_x"]
    top_y = obj["top_y"]
    gap = obj["gap"]
    pyautogui.click(top_x + (gap*x),top_y + (gap*y))

# RUN LOOP
time1 = time.time()
interactions = scanImage()
time2 = time.time()

print(f"Image size = {width} x {height}")
print("Click Gap =",draw_parems["gap"])
print(f"Total Interactions = {interactions} clicks")
print(f"Time Taken = {int(time2-time1)}s")