### used to take a simple image that is copied to clipboard
### and turn into clipart with transparent background ###

import subprocess, pyautogui, PIL, time, io
from pynput.keyboard import Key, Controller
keyboard = Controller()

### open paint ###
subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')

###use pyautogui to click on open paint3d ###
pyautogui.pause = 3.5
pyautogui.moveTo(1432, 200, duration = 1)
pyautogui.click()

### make python wait for slowass paint3d to open ###
time.sleep(4)

### paste image from clipboard ###
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release('v')
keyboard.release(Key.ctrl)

### use pyautogui to click on magic select ###
pyautogui.moveTo(692, 162, duration = 1)
pyautogui.click()
pyautogui.moveTo(1324, 502, duration = 1) 
pyautogui.click()


### ask for confirmation from user of selected outline ###
good_enough = input("Is the outline good enough? y/n ")
if good_enough == "y":
    pyautogui.moveTo(1585, 494, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(1571, 722, duration = 1)
    pyautogui.click()

bg_removed = input("Please select and delete the background. Then resize the image to fit the canvas. Press y when done. ")
if bg_removed == "y":
    ### make canvas transparent ###
    pyautogui.moveTo(1072, 83, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(1404, 317, duration = 1)
    pyautogui.click()
    ### save image ###
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)
    pyautogui.moveTo(869, 262, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(1565, 915, duration = 1)
    pyautogui.click()
    print("Type in file name and select correct folder. ")
    

