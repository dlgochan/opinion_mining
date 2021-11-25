import json

f_input = open("./twitter.json", mode="r")
f_output = open("C:/Users/osb04/Desktop/Vscode/Datamining/twitter.txt", mode="w", encoding='utf8')
str = []
tweets = []

str = f_input.readlines()

for j in str:
    tweets.append(json.loads(j))
############################################################
# 이제 tweets 변수에 dict(python의 자료형 중에 하나) 형식으로 json이 담김


# 예제
for j in tweets:
    # print(j['created_at']) # 각 트윗 생성일 출력
    # print(j['id_str']) # 각 트윗 id 출력
    # print(j['full_text']) # 각 트윗 글 출력
    f_output.write(j['full_text'])
    
print("END")
