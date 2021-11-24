import json
from konlpy.tag import Okt
okt = Okt()

f_input = open("hanspell.json", mode="r")

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
        if word[1] == 'Noun' or word[1] == 'Adjective':
            result.append(word[0])

print(result)
