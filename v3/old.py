print("Programmed Artist")
 
from PIL import Image
import time
import pyautogui
import os

pyautogui.PAUSE = 0.01
color_w = (255,255,255)
color_b = (128,128,128)
 
moveDist = 1
moveDist = int(input("enter move distance:"))


def getImageLink():
    cwd = os.path.dirname(os.path.abspath(__file__))
    img_link = os.path.join(cwd, "eren.jpg")
    return img_link

im = Image.open(getImageLink())
pix = im.load()
width,height = im.size
small_delay=0.1
 
def draw(x,y):
	if pix[x,y] < color_b:
		    if pix[x-1,y] < color_b:
			    #print(">>",x,",",y,"  -",pix[x,y],"           L")
			    pix[x,y] = color_w
			    pyautogui.move(-moveDist,0,small_delay)
			    draw(x-1,y)
		    elif pix[x,y+1] < color_b:
			    #print(">>",x,",",y,"  -",pix[x,y],"           D")
			    pix[x,y] = color_w
			    pyautogui.move(0,moveDist,small_delay)
			    draw(x,y+1)
		    elif pix[x+1,y] < color_b:
			    #print(">>",x,",",y,"  -",pix[x,y],"           R")
			    pix[x,y] = color_w
			    pyautogui.move(moveDist,0,small_delay)
			    draw(x+1,y)
		    elif pix[x,y-1] < color_b:
			    #print(">>",x,",",y,"  -",pix[x,y],"           U")
			    pix[x,y] = color_w
			    pyautogui.move(0,-moveDist,small_delay)
			    draw(x,y-1)
 
		    elif pix[x-1,y-1] < color_b:
			    pix[x,y] = color_w
			    pyautogui.move(-moveDist,-moveDist,small_delay)
			    draw(x-1,y-1)
		    elif pix[x-1,y+1] < color_b:
			    pix[x,y] = color_w
			    pyautogui.move(-moveDist,moveDist,small_delay)
			    draw(x-1,y+1)
		    elif pix[x+1,y+1] < color_b:
			    pix[x,y] = color_w
			    pyautogui.move(moveDist,moveDist,small_delay)
			    draw(x+1,y+1)
		    elif pix[x+1,y-1] < color_b:
			    pix[x,y] = color_w
			    pyautogui.move(moveDist,-moveDist,small_delay)
			    draw(x+1,y-1)
 
input("---Press to Start---")
t = time.localtime()
time1 = time.strftime("%H:%M:%S", t)
print(time1)
 
mouseX,mouseY = pyautogui.position()
for y in range(1,height):
    for x in range(1,width):
	    if pix[x,y] <= color_b:
		    #pyautogui.click(mouseX+(moveDist*x),mouseY+(moveDist*y))
		    pyautogui.mouseDown(mouseX+(moveDist*x), mouseY+(moveDist*y))	
		    draw(x,y)
		    pyautogui.mouseUp()
 
t = time.localtime()
time2 = time.strftime("%H:%M:%S", t)
print(time2)
 
print("")
input("Press any key to exit")