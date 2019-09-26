import pyautogui
import time


def letsbegin():
    # Climck on the URL bar for mailinator.co
    pyautogui.click(352,53) 
    time.sleep(1)
    pyautogui.typewrite('mailinator.com')
    pyautogui.press('enter')
    # Wait for the page load
    time.sleep(2)

    # Click on the mailinator search bar
    pyautogui.click(535,112)
    pyautogui.typewrite('modishahdoval02')
    pyautogui.press('enter')

    # Open a new tab for Zendesk
    pyautogui.hotkey('ctrl','t')
    # Wait for tab open
    time.sleep(1)
    # Click on the URL bar for Zendesk.com
    pyautogui.click(352,53) 
    time.sleep(1)
    pyautogui.typewrite('https://www.zendesk.com/register/')
    pyautogui.press('enter')
    # Wait for page load
    time.sleep(2)

    # Click on email form
    pyautogui.click(542,537)
    pyautogui.typewrite('modishahdoval02@mailinator.com')
    time.sleep(1)
    # Switch to Password field
    pyautogui.press('tab')
    pyautogui.typewrite('1234qwer!@#$')
    # Switch to Next button
    pyautogui.press('enter')
    time.sleep(2)

    # Click on the company field
    pyautogui.click(570,548)
    time.sleep(1)
    # Switch to number of employees selector
    pyautogui.press('tab')
    # Select 10-49 employees
    for i in range(7):
        pyautogui.press('down')
    time.sleep(1)
    # Switch to next button
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)

    # Click on First Name
    pyautogui.click(557,558)
    pyautogui.typewrite('ModiShah')
    time.sleep(1)
    # Switch to Last Name
    pyautogui.press('tab')
    pyautogui.typewrite('Doval02')
    time.sleep(1)
    # Switch to mobile number
    pyautogui.press('tab')
    pyautogui.typewrite('9414012307')
    time.sleep(1)
    # Switch to next button
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)

    # Click on Team Name
    pyautogui.click(557,612)
    pyautogui.typewrite('modishahdoval02')
    time.sleep(1)
    # Switch to Next Button
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(7)
    
    # Time to switch to previous tab
    pyautogui.hotkey('ctrl','shift','tab')
    time.sleep(2)
    # Click on the verification Mail
    pyautogui.click(518,268)
    # Wait for mail to open
    time.sleep(3)
    # Click on verification link
    pyautogui.click(330,392)
    time.sleep(10)


    






# To open firefox browser
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite('firefox')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

# Open the first tab as mailinator.com
letsbegin()