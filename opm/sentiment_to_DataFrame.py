#-*- coding: utf-8 -*-
import pandas as pd
import json

f = open("opm\sentiment_result.json", mode='r',encoding='UTF-8')

str = []
y=[]

str = f.readlines() 
for j in str:
    tmp = json.loads(j)
    if tmp['document']['sentiment'] == 'positive':
        y.append(1)
    elif tmp['document']['sentiment'] == 'negative':
        y.append(0)
    else:
        if tmp['document']['confidence']['negative'] > tmp['document']['confidence']['positive']:
            y.append(0)
        else:
            y.append(1)

columns=[]
df=pd.DataFrame(columns=columns)
df['y']=y
df.to_csv("opm\y_label.csv")