import pyscreenshot as ImageGrab
import keyboard
import time
import pyautogui

acomp = False
double = True
c = (670, 590, 1200, 591)
ofs = 5
xcold = 0


while True:
    if keyboard.is_pressed('x'):
        time.sleep(1)
        print("activated")
        turns = 0
        dly = 0
        while True:
            if keyboard.is_pressed('x'):
                time.sleep(1)
                print("deactivated")
                break
            else:
                im = ImageGrab.grab(c, childprocess=0)
                pixels = im.load()
                width, height = im.size
                onef = False
                for i in range(width):
                    r, g, b = im.getpixel((i, height-1))
                    if acomp == True:
                        if r < 10 and g < 30 and b < 60 or r > 14 and g > 127 and b > 236 and r < 29 and g < 253 and b < 255:
                            xcoord = i+670+ofs
                            ycoord = 591+dly
                            if xcoord != xcold and onef == False:
                                xcold = xcoord
                                pyautogui.click(xcoord, ycoord)
                                turns+=1
                                if double == True:
                                    break
                                onef = True
                            if double == True:
                                if onef == True:
                                    if xcoord > (xcold + 140):
                                        xcold = xcoord
                                        pyautogui.click(xcoord, ycoord)
                                        turns+=1
                                        break

                    if acomp == False:
                        if r < 10 and g < 30 and b < 60:
                            xcoord = i+670+ofs
                            ycoord = 591+dly
                            if xcoord != xcold and onef == False:
                                xcold = xcoord
                                pyautogui.click(xcoord, ycoord)
                                turns+=1
                                if double == True:
                                    break
                                onef = True
                            if double == True:
                                if onef == True:
                                    if xcoord > (xcold + 160):
                                        xcold = xcoord
                                        pyautogui.click(xcoord, ycoord)
                                        turns+=1
                                        break