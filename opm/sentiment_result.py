#-*- coding: utf-8 -*-
import pandas as pd
import json
from pandas import json_normalize

f = open("./opm/result.json", mode='r')

str = []
results=[]
sentiments=[]

str = f.readlines()
print(str[0][1:lent]) 
# for j in str:
#     tmp = json.loads(j)
#     sentiments.append(tmp)

# sentiments[0] = sentiments[0][1:len(sentiments[0])]
# print(sentiments[0])

# for s in sentiments:
#     print(s['document'])