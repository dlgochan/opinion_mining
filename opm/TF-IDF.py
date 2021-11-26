import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해
import json

str=[]
f_input = open("/content/drive/MyDrive/hanspell.json", mode="r")
f_input2 = open("/content/drive/MyDrive/okt.json", mode="r")
f_output = open("/content/drive/MyDrive/tfidf.json", mode="w", encoding='utf8')

str = f_input.readlines() #전체 트윗
str2 = f_input2.readlines() #단어(명사/형용사)

docs=[]
temp=[]
for j in str: #전체 트윗 list로 변환
    temp=json.loads(j)
    text = temp['text']
    docs.append(text)

tvocab=[]
temp=[]
for j in str2:
    temp=json.loads(j)
    if '명사' in temp.keys():
        text=temp['명사']
    else:
        text=temp['형용사']
    tvocab.append(text)
tvocab.sort()

#단어 중복 제거
vocab = list(set(tvocab))

# 총 문서의 수
N = len(docs) 

def tf(t, d):
    return d.count(t)

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df + 1))

def tfidf(t, d):
    return tf(t,d)* idf(t)

#tf 구하기
tf_result = []
for i in range(N): # 각 문서에 대해서 아래 명령을 수행
    tf_result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]        
        tf_result[-1].append(tf(t, d))


tf_ = pd.DataFrame(tf_result, columns = vocab)
print(tf_)

#idf
idf_result = []
for j in range(len(vocab)):
    t = vocab[j]
    idf_result.append(idf(t))

idf_ = pd.DataFrame(idf_result, index = vocab, columns = ["IDF"])
print(idf_)

#tf-idf
tfidf_result = []
for i in range(N):
    tfidf_result.append([])
    d = docs[i]
    print(d)
    for j in range(len(vocab)):
        t = vocab[j]
        #print(t)
        tfidf_result[-1].append(tfidf(t,d))
print(tfidf_result)

tfidf_ = pd.DataFrame(tfidf_result, columns = vocab)
print(tfidf_)

for result in tfidf_result:
    tmp = {'tfidf' : result}
    tmp2 = json.dumps(tmp) # dict -> json
    print(tmp['tfidf'], end='\n\n\n')  ## 값 잘 들어갔나 확인용
    f_output.write(tmp2)
    f_output.write('\n')