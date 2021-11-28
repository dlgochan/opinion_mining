# -*- conding: utf-8 -*-

import pandas as pd
import numpy as np
from konlpy.tag import Okt

with open('./korean_stopwords.txt', encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]


okt = Okt()

df = pd.read_csv("hanspell.csv")
# columns = []
# df2 = pd.DataFrame(columns=columns)



def okt_noun(text):
    tmp = []
    words = okt.pos(text)
    for word in words: 
        if word[1] == 'Noun' and len(word[0]) > 1 and word[0] not in stopwords:
            tmp.append(word[0])
    return tmp

def okt_verb(text):
    tmp = []
    words = okt.pos(text)
    for word in words: 
        if word[1] == 'Verb' and len(word[0]) > 1 and word[0] not in stopwords:
            tmp.append(word[0]) 
        elif word[1] == 'Adverb' and len(word[0]) > 1 and word[0] not in stopwords:
            tmp.append(word[0])
        elif word[1] == 'Adjective' and len(word[0]) > 1 and word[0] not in stopwords:
            tmp.append(word[0])     
    return tmp
    

df['okt_noun'] = df['han_text'].apply(lambda x : okt_noun(x))
df['okt_verb'] = df['han_text'].apply(lambda x : okt_verb(x)) # verb에 동사, 형용사, 부사

df.drop(['Unnamed: 0'], axis=1, inplace=True) # Unnamed column 제거
df.to_csv('words2.csv')
