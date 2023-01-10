import urllib.request, json, time, requests, random
from bs4 import BeautifulSoup
from os.path import exists

def TakeTest(HEADERS, LevelID, TopicID, QuizID):
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
    requests.post('https://www.testandtrack.io/index.php/profile/keepsessionalive', headers=HEADERS)

def urltemplate(level, topic="", quiz=""):
    baseurl = "https://www.testandtrack.io/index.php/student/test/"
    if topic == "": return baseurl+"/"+level
    else:
        if quiz == "":  return baseurl+"/"+level+"/"+topic
        else: return baseurl+"/"+level+"/"+topic+"/"+quiz


print("Welcome to JakeT23's TAT bot - For Educational Purposes only, 'q' to exit.")
if exists("answers.json") != True:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/answers.json", "answers.json")
    print("Notice - When using the 'a' flag please input the first test in that topic. - ALWAYS USE A FLAG")
    print("Notice - use the 's' flag for a single test use the 'a' flag for all of that topic. for example 'a https://www.testandtrack.io/index.php/studenttest/test/2/9/123'")
else:
    print("Notice - Always use a flag such as 'a' or 's' ")

loginUrl = "https://www.testandtrack.io/index.php/login/check"
cookiesForLogin = {"email": input("Enter Your Email: "), "password": input("Password echoes out coz fuk u :3c : "), "type":"S"}
loginResponse = requests.post(loginUrl, cookies=cookiesForLogin)

try:
    si = loginResponse.cookies["ci_session"] # the session cookie by itself
except KeyError: # no cookies sent back or cookie is not present
    print("Couldn't log u in, sux to suk")
    exit(1)
if (loginResponse.status_code != requests.codes.ok): # tbh no idea when this would happen
    print("Couldn't log u in, sux to suk")
    exit(1)

si = loginResponse.cookies["ci_session"]
session_cookies = "acceptcookie=Y;"+si

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Cookie": session_cookies,
        "Referer": "https://www.testandtrack.io/index.php/profile"}


while True:
    data = input("flag with URL: ")
    if data == "q":
        break
    urlnflag  = data.split(" ")
    flag = urlnflag[0].lower()
    url = urlnflag[1]
    if flag not in ["a", "s"]:
        print("ERROR > Please specify a flag ")
        print(">> use the 's' flag for a single test use the 'a' flag for all of that topic. for example 'a https://www.testandtrack.io/index.php/studenttest/test/2/9/123")
        quit()
    split_by_s = url.split("/")[::-1]
    QuizID  = split_by_s[0]
    TopicID = split_by_s[1]
    LevelID = split_by_s[2]
    quiz_indentifier = LevelID+"-"+TopicID+"-"+QuizID
    if LevelID != "2":
        print("Unsupported quiz, may not work. Only GCSE Quizes supported at the moment.")
        break
    if flag == "a":
        topicjson = json.loads(requests.post("https://www.testandtrack.io/index.php/profile/getQuizByTopic/"+TopicID, headers=HEADERS).text)
        ids = []
        for xy in topicjson:
            if int(xy["display_questions"]) > 0:
                ids.append(xy["id"])
        for i in ids:
            QuizID = i
            try:
                TakeTest(HEADERS, LevelID, TopicID, QuizID)
            except Exception as e:
                print("Probably finished some tests, unfortunately there was a bug: ", e)
            currurl = urltemplate(LevelID, TopicID, QuizID)
    elif flag == "s":
        TakeTest(HEADERS, LevelID, TopicID, QuizID)
