import urllib.request, json, time, requests, random
from bs4 import BeautifulSoup
from os.path import exists

cookies = ""


def urltemplate(level, topic="", quiz=""):
    baseurl = "https://www.testandtrack.io/index.php/student/test/"
    if topic == "": return baseurl+"/"+level
    else:
        if quiz == "":  return baseurl+"/"+level+"/"+topic
        else: return baseurl+"/"+level+"/"+topic+"/"+quiz


if exists("answers.json") != True:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/answers.json", "answers.json")
    print("Notice - remember to set your session cookies")
#    print("Notice - When using the 'a' tag please input the first test in that topic. - ALWAYS USE A FLAG")
#    print("Notice - use the 's' flag for a single test use the 'a' tag for all of that topic. for example 'a https://www.testandtrack.io/index.php/studenttest/test/2/9/123'")

url = input("url: ")
#data = input(": ")
#urlnflag  = url.split(" ")
#flag = urlnflag[0].lower()
#url = urlnflag[1]
#if flag not in ["a", "s"]:
#    print("ERROR > Please specify a flag ")
#    print(">> use the 's' flag for a single test use the 'a' tag for all of that topic. for example 'a https://www.testandtrack.io/index.php/studenttest/test/2/9/123")
#    quit()
split_by_s = url.split("/")[::-1]
QuizID  = split_by_s[0]
TopicID = split_by_s[1]
LevelID = split_by_s[2]
quiz_indentifier = LevelID+"-"+TopicID+"-"+QuizID


if LevelID != "2":
    print("Unsupported quiz, may not work. Only GCSE Quizes supported at the moment.")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Cookie": cookies,
        "Referer": "https://www.testandtrack.io/index.php/profile"}


r = requests.post('https://www.testandtrack.io/index.php/profile/givetest', headers=HEADERS, data={
            "submit": "Start+Test",
            "hdnpassreq": "N",
            "hdnispremium": "0",
            "hdnSelectedLevel": "",
            "hdnSelectedTopic": "",
            "hdnSelectedQuiz": "",
            "hdnSelectedLevelid": LevelID,
            "hdnSelectedTopicid": TopicID,
            "hdnSelectedQuizid": QuizID,
            "hdnquizurl": urltemplate(LevelID, TopicID, QuizID),
            "hdnquizurl-topic": urltemplate(LevelID, TopicID),
            "hdnquizurllevel":	urltemplate(LevelID),
            "ddllevel":	LevelID,
            "ddlTopic":	TopicID,
            "ddlQuiz":	QuizID,
            "hdnNextQuiz":	str(int(QuizID)+1),
})

answers = json.loads(open("answers.json").read())
soup = BeautifulSoup(r.text, "html.parser")

items = ["quizID", "total_ques", "total_marks", "total_time", "testID", "hdnTopic", "hdnLevel", "hdnNextQuiz","hdnSelectedLevel", "hdnSelectedTopic", "hdnSelectedQuiz", "hdnuseremail"]
values = []
for i in items:
    values.append(soup.findAll("input", {"name":i})[0].get('value'))

datas = dict(zip(items, values))

for i in answers[quiz_indentifier].keys():
    datas[i] = answers[quiz_indentifier][i][0]

timett = random.uniform(7.225, 25.231)

print("Inputting answers, This will take in excess of", timett, "seconds")
time.sleep(timett)
requests.post('https://www.testandtrack.io/index.php/profile/giveTestDemo/'+datas["quizID"], headers=HEADERS, data=datas)
