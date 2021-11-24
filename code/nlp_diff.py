import json

f_okt = open('okt.json', mode='r')
f_soy = open('soynlp+okt.json', mode='r')

okt_words = []
soy_words = []

for word in f_okt.readlines():
    okt_words.append(json.loads(word))
for word in f_soy.readlines():
    soy_words.append(json.loads(word))

okt = []
soy = []

for i in range(len(okt_words)):
    for key, value in okt_words[i].items():
        okt.append(value)

for i in range(len(soy_words)):
    for key, value in soy_words[i].items():
        soy.append(value)

# 차집합
print(list(set(soy).difference(okt)))
print(list(set(okt).difference(soy)))

        

