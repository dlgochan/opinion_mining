import json

f = open("./twitter.json", mode="r")
str = []
tweets = []

str = f.readlines()

for j in str:
    tweets.append(json.loads(j))
############################################################
# 이제 tweets 변수에 dict(python의 자료형 중에 하나) 형식으로 json이 담김


# 예제
for j in tweets:
    print(j['full_text'])