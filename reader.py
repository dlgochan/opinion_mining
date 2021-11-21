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
    # print(j['created_at']) # 각 트윗 생성일 출력
    # print(j['id_str']) # 각 트윗 id 출력
    print(j['full_text']) # 각 트윗 글 출력