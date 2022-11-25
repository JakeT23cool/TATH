# JakeT23's Test And Track Bot!
*Educational Purposes Only!*

[Try it Online!](https://replit.com/@jaket23/JakeT23s-Test-and-Track-Bot)

work in progress.

# How to run the python version:

## Dependencies:
- BeautifulSoup
- Requests


Install by running in the command-line:
- pip install bs4 requests

## Downloading the script
Find the download link the releases tab.

[Download](https://github.com/JakeT23cool/TATH/releases/download/official/answer.py)
## Getting the session variable

You will have to repeat this step everytime you relogin on test&track

1. First login to test and track

2. Click F12 to open Inspect element

3. Navigate to the network tab

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/1.png">

5. click 'reload'

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/2.png">

7. then click on the tab that says student - should be first

8. copy all the data from the 'cookie' variable

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/3.png">

9. paste the data into the session cookies prompt when you run the program

## Completing the test
10. Go to the test that that you want to do (remember - individual test!) or when using the 'a' flag go to the test at the start of the topic.

11. click the mobile 'share' icon (this will copy the link)

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/5.png">

12. Now run the program using python (either using idle or the command line tool) and paste the url

<hr>

## How to update the program
- Delete the answers.json file (for answer updates)
- Reinstall (for answer updates and code updates)

## Roadmap
- Easy GUI for login and test completion
- Support for all T&T Topics (besides GCSE)
