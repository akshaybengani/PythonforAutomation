# T-Shirt Generator
This project focuses on generating T-Shirts in the most popular events Hacktoberfest and Microsoft Contributor Reward.
<br> Both of these programs provide T-Shirt by opeing pull requests.
<br> This program will focus on generating fake outlook accounts and GitHub Accounts bypassing the Github Captcha and commiting on the repositories.

## System Requirements
To use this we need some basic requirements like a working computer with a proper internet connection.
#### Software Requirements
* Python 3.7
* pip installed
* pip packages like xlrd, pyautogui
* Windows 10 required
* Chrome browser

## Features
Some great features like Excel Sheet data entry, page loading validations, GitHub Captcha Solver, etc etc.

### Excel Account Information
Everytime we run the program it will create an excel sheet
name + timeStrap in the file this will help in maintaining
the records of each session accounts

### Page Loading Validations
Will use image recorgination to validate that page is loaded or not
by using screenshot generator  and comparing that to the required webpage

### Captcha Solver for Github
This will detect the images by their position and will compare that with predefined dataset to make sure it is the same picture or not
if not then change the picture orientation to solve the captcha

### Data inside the book
This will contain data blocks nameing 
<pre>
Outlook Account 
    FName : Rahul 
    LName : Gandhixxx00
    Username : username series starts from : rahulgandhixxx00
    Password : Same Password for all the accounts : 6A9dX9qtpZYqzG2
    Status Check : Created/Error
    Date of Account Creation : 
Github Account
    Username : username series starts from : mescript3600user00
    Password : Same Password for all the accounts : 6A9dX9qtpZYqzG2
    Status : Created/Error
    Date of Account Creation :
    Email Verification Status : Verified using outlook
Hacktoberfest Registration
    Github Login Check :
    Outlook Login Check :
    Registration Check :
Commit Generator
    Commit Count : Total Count must be 10
    Check Commit count to proceed to next
</pre>

### Checks Validation
Checks will be validated using OpenCV and Machine Learning


