import pynput
import time
import os
from pynput.keyboard import Key, Controller
keyboard = Controller()
k = keyboard
key = Key

def alt_tab():
    k.press(key.alt)
    k.press(key.tab)
    k.release(key.alt)
    k.release(key.tab)

def ctrl_t():
    k.press(key.ctrl)
    k.press('t')
    k.release(key.ctrl)
    k.release('t')

def ctrl_w():
    k.press(key.ctrl)
    k.press('w')
    k.release(key.ctrl)
    k.release('w')

def tab():
    k.press(key.tab)
    k.release(key.tab)

# FName = mescript
# LName = 3600user00
# Email = mescript3600user00@gmail.com
# Pass = 6A9dX9qtpZYqzG2

# time.sleep(2)
alt_tab()






