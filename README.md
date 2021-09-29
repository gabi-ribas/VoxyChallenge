# VoxyChallenge
Coding challenge for Voxy

**This document describes how to install the required components and run the automated test cases**


## Step 1. Install the latest release of python 3.8
*If you already have python 3.8 installed, please ignore this step*

-   If you’re a Mac OS user: https://www.python.org/downloads/macos/
    
-   If you’re a Windows user: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
    
-   If you’re a Linux user: https://www.python.org/downloads/source/
    



## Step 2. Install PyCharm Community from:
*You may use any python IDE of your liking, here we will be using PyCharm CE*

-   https://www.jetbrains.com/pycharm/download/

Make sure to pick your Operational System and download the “Community” version

  

## Step 3. Clone the SeleniumProject folder in a repository of your choice

  

## Step 4. Open the cloned project

Open Pycharm CE, click on “file” and choose “open”. From there open the SeleniumProject folder you just cloned

  

## Step 5. Set up a venv

(For a more detailed process, please check: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

On Pycharm CE:

1.  Click on “File”
    
2.  Go to “New Projects Settings”
    
3.  Go to “Preferences for New Projects”
    
4.  Go to “Python Interpreter”
    
5.  Click on the cogwheel icon (around the top right of the current popup window)
    
6.  Click on “add”
    
7.  Choose “Virtualenv” environment on the left
    
8.  Choose “New Environment”
    
9.  Choose the location for you virtual environment (must be a new folder)
    
10.  Choose Python 3.8 as the interpreter
    
11.  Leave all other options unchecked
    
12.  Click on “ok”
    

## Step 6. Use your new venv

On Pycharm CE:

1.  Click “Run”
    
2.  Go to “Edit Configurations”
    
3.  Assure your “Script Path” points to [the repository where you cloned the project]/seleniumProject/main.py, otherwise, set it there
    
4.  Assure the “Working Directory” points to [the repository where you cloned the project]/seleniumProject, otherwise, set it there
    
5.  Set the value of “Python Interpreter” to the venv you just created
    
6.  Click on ok
    

## Step 7. Download ChromeDriver

This test is intended for the google Chrome Browser, if you don’t have it, install it from here [https://www.google.com/intl/en-US/chrome/](https://www.google.com/intl/en-US/chrome/)

1.  Open Google Chrome and go to “settings”, “help” then “about google chrome”
    
2.  Take note of the chrome version you see there
    
3.  Go to [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and download the ChromeDriver corresponding to the version of your browser (If you can’t find it, you must update google chrome)
    
4.  Extract the ChromeDriver from the downloaded file and move it to the same directory as where your python 3.8 file is: inside the folder of your new venv
    

## Step 8. Download Selenium

On Pycharm CE

1.  On the bottom of the window, to the left, click on “Terminal”
    
2.  Use the command “pip install selenium”
    

## Step 9. Run your test

Press the “play” button either on the “Run” menu or on the top right of the window

## Why were these testes chosen?
Due to data availability (no access to active voxy accounts), the possible tests left to be automated were the ones that were intended to fail, from those I decided to choose ones that would provide a different challenge on asserting the results: one requiring the verification of the presence of a pop-up and the other needing to have the inability to input data in a field checked.
The chosen tests for such were both from the *User attempts to login via email* scenario:

*Test case 5: User attempts to login with a valid email address, but not linked to any valid voxy accounts*

*Test case 6: User attempts to input data on the "email" field while having the "mobile number" option selected*
