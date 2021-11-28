#-*- coding: utf-8 -*-
import pandas as pd
import json
from pandas import json_normalize

f = open("C:/Users/wngus/Documents/GitHub/opinion_mining/opm/result.json", mode='r',encoding='utf8')

str = []
results=[]
sentiments=[]

str = f.readlines() 
for j in str:
    tmp = json.loads(j)
    sentiments.append(tmp)

for s in sentiments:
    print(s['document'])