import json
from konlpy.tag import Okt
okt = Okt()

f_input = open("hanspell.json", mode="r")
f_output = open("okt.json", mode = "w")

str = []
tweets = []

str = f_input.readlines() 

for j in str:
    tweets.append(json.loads(j)) # json -> dict


result = []
# 예제
for j in tweets:
    words = okt.pos(j['text'])
    
    # 명사나 형용사만 추출
    for word in words: 
        if word[1] == 'Noun':
            tmp = {'명사' : word[0]}
            tmp2 = json.dumps(tmp)
            f_output.write(tmp2)
            f_output.write('\n')
        elif word[1] == 'Adjective':
            tmp = {'형용사' : word[0]}
            tmp2 = json.dumps(tmp)
            f_output.write(tmp2)
            f_output.write('\n')
