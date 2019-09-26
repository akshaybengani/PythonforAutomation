import pyautogui
import time

pyautogui.hotkey("alt","tab")
time.sleep(1)
while True:
    pyautogui.typewrite("Hi bhaiya")
    pyautogui.press("enter")