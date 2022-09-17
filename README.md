# TAT H
*Educational Purposes Only!*

work in progress
Refined JS version coming soon
# How to run the proof-of-concept python version:

## Dependencies:
- BeautifulSoup
- Request


Install by running:
- pip install bs4 requests

## Downloading the script
Find in the releases tab in github
[Releases](https://github.com/JakeT23cool/TATH/releases)
## Getting the session variable

You will have to repeat this step everytime you relogin on test&track

1. First login to test and track

2. Click F12 to open Inspect element

3. Navigate to the network tab

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/1.png">

5. click 'reload'

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/2.png">

7. then click on the tab that says student - should be first

8. copy and paste all the data from the 'cookie' variable

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/3.png">

10. input the data into the cookies variable in the python source code

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/4.png">

## Completing the test
9. Go to the test that that you want to do (remember - individual test!)

10. click the mobile 'share' icon (this will copy the link)

<img src="https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/src/5.png">

12. Now run the program using python (either using idle or the command line tool) and paste the url

# limitations
- only works with the majority of GCSE quizes
- may not work with Worded answers
