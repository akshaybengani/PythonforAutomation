from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="E:\\ProgrammingData\\Automation\\geckodriver.exe")

# Window index 0 created
driver.get("https://www.mailinator.com")
title = driver.title
print("Title is :"+title)

time.sleep(2)

# Window index 1 created
driver.execute_script("window.open('http://www.twitter.com','new window')")
# this is to switch to a new window
driver.switch_to.window(driver.window_handles[1])
title = driver.title
print("Title is :"+title)

time.sleep(2)

# Window index 2 created
driver.execute_script("window.open('http://www.akshaybengani.me','new window')")
# this is to switch to a new window
driver.switch_to.window(driver.window_handles[2])
title = driver.title
print("Title is :"+title)

time.sleep(2)

# Window index 3 created
driver.execute_script("window.open('http://www.github.com/akshaybengani','new window')")
# this is to switch to a new window
driver.switch_to.window(driver.window_handles[3])
title = driver.title
print("Title is :"+title)