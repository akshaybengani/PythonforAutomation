import time
from selenium import webdriver
import re

# Note using executable_path is important else it will give error for file not found
driver = webdriver.Firefox(executable_path="E:\\ProgrammingData\\Automation\\geckodriver.exe")

# This is for opening a website note right now we can only open one website at a time
# The last line for the program with get function will be used.
driver.get("http://www.airindia.in/customer-support.htm")

# In order to print the title of the webpage
print(driver.title)

# To get the page source code use this method
doc = driver.page_source

# \w means word
# \.- means these symbols can contain
# +@ means this symbol must be present
# doc is the text from where we need to find
emails = re.findall(r'[\w\.-]+@[\w\.-]+',doc)

# Since emails can be multiple as such re gives data in list
for email in emails:
    print(email)

# \d is for a number
# {3} is the length of number type
# + is for connecting these expressions
# empty space is to specify that the next character is space
phones = re.findall(r'[\d]{4}[ ]+[\d]{3}[ ]+[\d]{4}',doc)

for phone in phones:
    print(phone)
