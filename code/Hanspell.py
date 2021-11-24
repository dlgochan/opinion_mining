import json
from hanspell import spell_checker

f_input = open("rm_dup.json", mode="r")
f_output = open("hanspell.json", mode="w")
str = []
tmp = []

str = f_input.readlines()

for j in str:
    tweet = json.loads(j)
    text = tweet['text']
    spelled_text = spell_checker.check(text) # 맞춤법 교정
    tmp = {'text' : spelled_text.checked} # checked > 교정 결과
    tmp2 = json.dumps(tmp)
    print(tmp) # 잘 들어갔나 확인용
    f_output.write(tmp2)
    f_output.write('\n')
