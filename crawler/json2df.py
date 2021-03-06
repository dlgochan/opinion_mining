import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



f_input = open("./omicron_deduplication.json", mode="r")
# f_output = open("df.json", mode="w", encoding='utf8')
str = []
tweets = []

str = f_input.readlines() 

for j in str:
    tweets.append(json.loads(j)) # json -> dict


############################################################
# 이제 tweets 변수에 dict(python의 자료형 중에 하나) 형식으로 json이 담김

#json to dataframe

df = pd.DataFrame(columns=['text'])
i=0
for tweet in tweets:
    row = [tweet['text']]
    series = pd.Series(row, index=df.columns)
    df = df.append(series, ignore_index=True)
    i+=1

df.to_csv("../nlp/tweets.csv")
df.to_csv("../nlp/omicron.csv")

# 이제부터 자연어 처리 시작
