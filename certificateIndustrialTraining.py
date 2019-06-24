import pyautogui
import time

def generateme():
    # Select new entry and copy it
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','c')

    # Switch to photoshop for 1st time
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.click(565,360)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('ctrl','shift','s')

    time.sleep(1)
    pyautogui.click(482,527)
    time.sleep(1)
    pyautogui.click(354,445)
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

# Set tab index
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.click(167,750)
time.sleep(1)

i = 0
while i<42:
    generateme()
    i=i+1

    








