import time
from selenium import webdriver
# We can use this to send keyboard keys to the browser
from selenium.webdriver.common.keys import Keys
import pyautogui

# This is to setup the webdriver for firefox
driver = webdriver.Firefox(executable_path="E:\\ProgrammingData\\Automation\\geckodriver.exe")

# This is to open our first webpage in 1st tab index 0
driver.get("https://www.mailinator.com")

# This is to type something on the textfield
driver.find_element_by_xpath('//*[@id="inboxfield"]').send_keys("rahulgandhiscript01")

# This is to click on the go button
driver.find_element_by_xpath('//*[@id="go_inbox1"]').send_keys(Keys.ENTER)


# We have opened a new tab then switched to index 1 and opened a url on that
pyautogui.hotkey('ctrl','t')
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.github.com/akshaybengani")

# We have opened a new tab then switched to index 2 and opened a url on that
pyautogui.hotkey('ctrl','t')
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.linkedin.com/in/akshaybengani")



'''
def checkme():
    try:
        inputfield = driver.find_element_by_xpath('//*[@id="inboxfield"]')
    except:
        time.sleep(1)
        print("not found yet...")
        checkme()
checkme()
inputfield.send_keys()
'''

# elem.click()
# elem.text
# elem.send_keys('Search String')
# elem.send_keys(Keys.ENTER)
