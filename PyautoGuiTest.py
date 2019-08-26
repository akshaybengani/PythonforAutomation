import pyautogui
import time

pyautogui.FAILSAFE = False

def completeAction():
    time.sleep(2)

# Index Setup
# pyautogui.hotkey('alt','tab')
# time.sleep(1)
# pyautogui.click() # Click on the program
# time.sleep(1)

i = 0
process = 10
time.sleep(3)
for i in range(10):
    time.sleep(1)
    pyautogui.hotkey('alt','tab')
    print("Rocking "+str(i))
    time.sleep(1)
    pyautogui.hotkey('alt','tab')    
    print("Dashing "+str(i))



accID = 10
accEnd = 20

# while accID < accEnd:
#     completeAction(accID)
#     accID = accID + 1
