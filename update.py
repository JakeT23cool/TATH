import requests
resp = requests.get("https://raw.githubusercontent.com/JakeT23cool/TATH/stablebranch/answers.json").content
with open("answers.json","wb") as File:
  File.write(resp)
