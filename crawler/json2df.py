import json



f_input = open("./rm_dup.json", mode="r")
f_output = open("df.json", mode="w", encoding='utf8')
str = []
tweets = []

str = f_input.readlines() 

for j in str:
    tweets.append(json.loads(j)) # json -> dict


############################################################
# 이제 tweets 변수에 dict(python의 자료형 중에 하나) 형식으로 json이 담김

for tweet in tweets:
    tmp = {'text' : remove}
    tmp2 = json.dumps(tmp) # dict -> json
    print(tmp['text'], end='\n\n\n')  ## 값 잘 들어갔나 확인용
    f_output.write(tmp2)
    f_output.write('\n')

print("END")
