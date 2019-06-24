import pyautogui

# This will return the mouse position in x and y values
mousePos = pyautogui.position()
# This will return screen size (x,y)
pyautogui.size()
# This will click on the position entered here
pyautogui.click(100,100)
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# To type on the board use
pyautogui.typewrite("Anything over here will be typed")
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)
# Moving the mouse to the upper left to raise a exception
    #   That can abort the program
pyautogui.FAILSAFE = True
# move mouse to XY coordinates over num_second seconds
pyautogui.moveTo(x, y, duration=num_seconds)
# move mouse relative to its current position
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
# drag mouse to XY
pyautogui.dragTo(x, y, duration=num_seconds)  
# drag mouse relative to its current position
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  
# Hold click to somewhere
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)
# Positive scrolling will scroll up, negative scrolling will scroll down:
pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
pyautogui.hscroll(10)   # scroll right 10 "clicks"
pyautogui.vscroll(10)   # scroll top 10 "clicks"
# To print all types of key names
pyautogui.KEYBOARD_KEYS
# Hotkeys
pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
# Press Key
pyautogui.press('enter')  # press the Enter key
# Hold key pressed or down
pyautogui.keyDown('shift')  # hold down the shift key
# Release Key pressed
pyautogui.keyUp('shift')  # Release the shift key


