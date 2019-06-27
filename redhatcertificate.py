import pyautogui
import time
import pyperclip

def generateme(id):
    # Switch to Excel
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    # Go To Next Cell
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','c')
    # Switch to Photoshop
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    # Click on Name
    pyautogui.click(320,370)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('ctrl','enter')
    time.sleep(2)
    # Save File
    pyautogui.hotkey('ctrl','shift','s')
    time.sleep(2)
    # Write File Name
    name = pyperclip.paste()
    name = name[:-2]
    pyautogui.typewrite(str(id))
    pyautogui.typewrite(" ")
    pyautogui.typewrite(name)
    # Choose JPEG File
    time.sleep(1)
    pyautogui.click(397,524)
    time.sleep(2)
    pyautogui.click(368,327)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    print(name," Your certificate is ready for printing")   
    

# Set tab index
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.click(243,751)
time.sleep(1)

id = 37
i = 0
while i < 34:
    generateme(id)
    id = id + 1
    i = i + 1