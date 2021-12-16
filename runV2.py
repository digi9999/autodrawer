print("Autodrawer v2 (JPG images only)")

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
    "scale": float(input("scale:")),
    "top_x": pyautogui.position().x,
    "top_y": pyautogui.position().y
}

color_0 = (0,0,0)
color_1 = (64,64,64)
color_2 = (128,128,128)

color_w = (255,255,255)

def scanImage():
    for y in range(0, height, 1):
        print(f"running.. {math.trunc(y/height * 100)}% ")
        for x in range(0,width,1):

            # CUSTOM FAIL SAFE BUTTON
            if keyboard.is_pressed("esc"):
                time.sleep(1)
                break

            if pix[x,y] >= color_0 and pix[x,y] <= color_2:
                run_loop(x,y,color_0,color_2, draw_parems)

        os.system('cls||clear')
    print("Completed!")

def run_loop(x,y,color_a,color_b, obj,):
    a = x
    b = y
    line_length = 0
    while x < width and pix[x+1,y] >= color_a and pix[x+1,y] <= color_b:
        
        pix[x,y] = color_w
        x += 1
        line_length += 1

    pyautogui.moveTo(obj["top_x"] + a, obj["top_y"] + b)
    pyautogui.drag(line_length, 0)

# RUN LOOP
time1 = time.time()
interactions = scanImage()
time2 = time.time()

print(f"Image size = {width} x {height}")
print("Scale =",draw_parems["scale"])
print(f"Time Taken = {int(time2-time1)}s")