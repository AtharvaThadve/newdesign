import time
import pyautogui
import os
from AppOpener import *

os.startfile("C:/Users/Admin/Documents/New folder1")
pyautogui.keyDown('win')
pyautogui.press(['up'])
pyautogui.keyUp('win')
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'f4')
os.startfile("C:/Users/Admin/Documents/New folder2")
pyautogui.keyDown('win')
pyautogui.press(['up'])
pyautogui.keyUp('win')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("F5")
pyautogui.press("F5")
time.sleep(3)

time.sleep(3)
pyautogui.press("esc")
pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.hotkey('win', 'd')


# Opening github
open("github desktop")
time.sleep(20)
pyautogui.keyDown('win')
pyautogui.press(['up'])
pyautogui.keyUp('win')


time.sleep(2)
pyautogui.moveTo(91, 552, duration=1)
pyautogui.click(91, 552)
pyautogui.write('Version--', interval=0.25)
pyautogui.moveTo(47, 594, duration=1)
pyautogui.click(47, 594)
pyautogui.write('Editing CSS...', interval=0.25)
pyautogui.moveTo(116, 701, duration=1)
pyautogui.click(116, 701)
time.sleep(4)
pyautogui.moveTo(564, 48, duration=1)
pyautogui.click(564, 48)
time.sleep(4)
pyautogui.moveTo(564, 48, duration=1)
pyautogui.click(564, 48)

# Coming to Home
time.sleep(4)
pyautogui.hotkey('alt', 'f4')
time.sleep(1)
pyautogui.hotkey('alt', 'f4')

# Alert
pyautogui.alert('Files had been copied & pushed up to Github.\nShuting Down...\nBye Bye')

time.sleep(2)
pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.hotkey('win', 'd')

# Shuting Down
pyautogui.moveTo(564, 48, duration=1)
pyautogui.click(564, 48)
pyautogui.hotkey('alt', 'F4')
time.sleep(1)
# Point(x=856, y=299)
pyautogui.moveTo(856, 299, duration=1)
pyautogui.click(856, 299)
# Point(x=646, y=377)
pyautogui.moveTo(646, 377, duration=1)
pyautogui.click(646, 377)
pyautogui.press("ENTER")