import json
from typing import Collection

# f_input = open("./twitter.json", mode="r")
f_input = open("./omicron.json", mode="r")

# f_output = open("deduplication.json", mode="w", encoding='utf8')
f_output = open("omicron_deduplication.json", mode="w", encoding='utf8')
str = []
tweets = []

str = f_input.readlines() 

for j in str:
    tweets.append(json.loads(j)) # json -> dict


############################################################
# 이제 tweets 변수에 dict(python의 자료형 중에 하나) 형식으로 json이 담김

tmp = []
# 예제
for j in tweets:
    tmp.append(j['full_text'])
    # print(j['created_at']) # 각 트윗 생성일 출력
    # print(j['id_str']) # 각 트윗 id 출력
    # print(j['full_text']) # 각 트윗 글 출력
    # f_output.write(j['full_text'])

removes = list(set(tmp)) # 중복 제거한 문자열(트윗) 리스트

for remove in removes:
    tmp = {'text' : remove}
    tmp2 = json.dumps(tmp) # dict -> json
    print(tmp['text'], end='\n\n\n')  ## 값 잘 들어갔나 확인용
    f_output.write(tmp2)
    f_output.write('\n')

print("END")
