print("Autodrawer v3 (JPG images only)")

from PIL import Image
import time

import pyautogui
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

import os
import math
import keyboard

import sys
sys.setrecursionlimit(1500)


def getImageLink():
    cwd = os.path.dirname(os.path.abspath(__file__))
    img_link = os.path.join(cwd, "eren.jpg")
    return img_link

myImg = Image.open(getImageLink())
pix = myImg.load()
width,height = myImg.size

draw_parems = {
    "scale": float(input("dist:")),
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
                pyautogui.moveTo(draw_parems["top_x"] + x, draw_parems["top_y"] + y)
                run_trace(x,y,color_0,color_2, draw_parems)

        os.system('cls||clear')
    print("Completed!")

def run_trace(x,y,color_a,color_b, obj):
    d = obj["scale"]
    delay = 0.01
    allow = True
    if pix[x,y] >= color_a and pix[x,y] <= color_b and x < width and y < height and x >= 0 and y > 0:

        if x >= 0 and pix[x-1,y] >= color_a and pix[x-1,y] <= color_b:
            print("x-1") if allow else False
            pix[x,y] = color_w
            pyautogui.move(-d,0,delay)
            run_trace(x-1,y,color_a,color_b, obj)

        elif y < height and pix[x,y+1] >= color_a and pix[x,y+1] <= color_b:
            print("y+1") if allow else False
            pix[x,y] = color_w
            pyautogui.move(0,d,delay)
            run_trace(x,y+1,color_a,color_b, obj)

        elif x < width and pix[x+1,y] >= color_a and pix[x+1,y] <= color_b:
            print("x+1") if allow else False
            pix[x,y] = color_w
            pyautogui.move(d,0,delay)
            run_trace(x+1,y,color_a,color_b, obj)

        elif y >= 0 and pix[x,y-1] >= color_a and pix[x,y-1] <= color_b:
            print("y-1") if allow else False
            pix[x,y] = color_w
            pyautogui.move(0,-d,delay)
            run_trace(x,y-1,color_a,color_b, obj)

# RUN PROGRAM
time1 = time.time()
interactions = scanImage()
time2 = time.time()

print(f"Image size = {width} x {height}")
print("Scale =",draw_parems["scale"])
print(f"Time Taken = {int(time2-time1)}s")