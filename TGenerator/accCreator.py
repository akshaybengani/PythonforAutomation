import pyautogui
import time
import os
from xlwt import Workbook
import datetime
wb = Workbook()

print("Welcome to Outlook and Github Account Generator")
dirPath = os.getcwd()
dirName = "OutGit "+datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
os.mkdir(dirName)
# Creates a new Sheet
msheet = wb.add_sheet("Accounts")
msheet.write(0,0,"Username")
msheet.write(0,1,"Email")
msheet.write(0,2,"Password")
# Saves the file
wb.save(dirPath+"\\"+'Credentials.xls')

def protonMail(accno,crow):
    pyautogui.hotkey('alt','tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','t')
    time.sleep(0.5)
    pyautogui.click(313,50) #urlBarPos
    pyautogui.typewrite('https://protonmail.com/signup')
    time.sleep(0.5)
    pyautogui.press('enter')
    # Now the webpage will load so need time for next task
    time.sleep(5)

    pyautogui.click(1118,635)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)   
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('del')
    pyautogui.typewrite('rahulgandhiscript'+accno)
    pyautogui.press('tab')
    pyautogui.press('tab') 
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('del')
    pyautogui.typewrite('6A9dX9qtpZYqzG2')
    pyautogui.press('tab') 
    pyautogui.press('tab')
    pyautogui.typewrite('6A9dX9qtpZYqzG2')
    pyautogui.press('tab') 
    pyautogui.press('tab')
    pyautogui.press('tab') 
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.click(827,220) # Save password
    pyautogui.press('tab') 
    pyautogui.press('tab')
    pyautogui.press('tab') 
    pyautogui.press('tab')
    pyautogui.press('tab') 
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space') 
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.click(989,985) # Finish button 
    msheet.write(crow,0,"rahulgandhiscript"+accno)
    msheet.write(crow,1,"6A9dX9qtpZYqzG2")
    wb.save(dirPath+"\\"+'Credentials.xls') 

def outlookMail(accno,crow):
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl','t')
    time.sleep(1)
    pyautogui.click(313,50) #urlBarPos
    pyautogui.typewrite('https://signup.live.com/signup')
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.click(534,463)
    pyautogui.typewrite('rahulgandhiscript'+accno)
    pyautogui.click(797,516)
    time.sleep(2)
    pyautogui.typewrite('6A9dX9qtpZYqzG2')
    pyautogui.click(797,576)
    time.sleep(2)
    pyautogui.typewrite('Rahul')
    pyautogui.press('tab')
    pyautogui.typewrite('gandhiscript'+accno)
    pyautogui.click(810,545)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.typewrite('1990')
    time.sleep(1)
    pyautogui.click(797,570)
    input("Press a key to proceed ")
    #time.sleep(30)
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    pyautogui.hotkey('ctrl','w')
    time.sleep(1)
    pyautogui.hotkey('ctrl','t')
    time.sleep(2)
    pyautogui.click(313,50) #urlBarPos
    pyautogui.typewrite('http://outlook.com/')
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.click(954,519)
    time.sleep(2)
    pyautogui.click(954,519)
    time.sleep(2)
    pyautogui.click(952,411)
    time.sleep(2)
    pyautogui.click(952,411)
    time.sleep(2)
    pyautogui.click(952,411)
    time.sleep(2)
    pyautogui.click(952,411)
    time.sleep(2)
    pyautogui.click(955,516)
    time.sleep(15)
    pyautogui.click(681,563)
    time.sleep(2)
    pyautogui.click(1028,196)
    time.sleep(3) # now outlook mail is logined and setup
    pyautogui.hotkey('ctrl','t') # Lets create a github account
    time.sleep(2)
    pyautogui.click(313,50) #urlBarPos
    pyautogui.typewrite('https://github.com/')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(1257,136)
    time.sleep(4)
    pyautogui.typewrite('rahulgandhiscript'+accno)
    pyautogui.press('tab')
    pyautogui.typewrite('rahulgandhiscript'+accno+'@outlook.com')
    pyautogui.press('tab')
    pyautogui.typewrite('6A9dX9qtpZYqzG2')
    input("Press a key to proceed ")
    # Do fill the captcha and proceed next to two pages till it
    # asks for verify the email address
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    pyautogui.hotkey('ctrl','shift','tab')
    
    pyautogui.press('f5')
    time.sleep(6) # Wait to load inbox
    pyautogui.click(90,570) # Junk Email
    time.sleep(4)
    pyautogui.click(330,353) # email click
    time.sleep(2)
    pyautogui.click(745,611) # Verify button click
    time.sleep(3)
    print('Account Created Successfully')
    pyautogui.click(1326,135)
    time.sleep(2)
    pyautogui.click(1189,516) # Github Logout
    time.sleep(2)
    pyautogui.hotkey('ctrl','w')
    time.sleep(2)
    #pyautogui.click(1137,127) # Bug in line
    # 16 tabs to go
    i = 0
    while i < 16:
        pyautogui.press('tab')
        time.sleep(0.5)
        i = i + 1
    time.sleep(2)
    pyautogui.click(1094,388) # Logout button
    time.sleep(2)
    pyautogui.hotkey('ctrl','w')
    time.sleep(2)

    pyautogui.hotkey('ctrl','w')
    time.sleep(2)
    print("Task Completed")




accno = '16'
crow = '1'
outlookMail(accno,crow)

# protonMail(accno,crow)







