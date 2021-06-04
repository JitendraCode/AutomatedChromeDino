import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    return

def isCollide(data):
        #birds
        for i in range(115, 220):
            for j in range(407, 525):
                if data[i,j]<100:
                    hit("up")
                    return
        #cactus
        for i in range(115, 220):
            for j in range(407, 525):
                if data[i,j]==0:
                    hit("up")
                    return
        return 
     
if __name__=="__main__":
    print("Hey ! Dino Game about to start in 3 seconds")
    time.sleep(2)
    hit('up')
    
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
 