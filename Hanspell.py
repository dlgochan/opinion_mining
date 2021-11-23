import json
from hanspell import spell_checker

f_input = open("./twitter.json", mode="r")
str = []
tweets = []

str = f_input.readlines()

for j in str:
    tweets.append(json.loads(j))


for j in tweets:
    sent = j['full_text']
    spelled_sent = spell_checker.check(sent)
    hanspell_sent = spelled_sent.checked
    print(hanspell_sent + '\n')