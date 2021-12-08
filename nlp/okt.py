# -*- conding: utf-8 -*-

import pandas as pd
from konlpy.tag import Okt

with open('./nlp/korean_stopwords.txt', encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]


okt = Okt()

df = pd.read_csv("./nlp/omicron_hanspell.csv", index_col=0)

def okt_noun(text):
    tmp = []
    words = okt.pos(text)
    for word in words: 
        if word[1] == 'Noun' and len(word[0]) > 1 and word[0] not in stopwords:
            tmp.append(word[0])
    return tmp

# def okt_verb(text):
#     tmp = []
#     words = okt.pos(text)
#     for word in words: 
#         if word[1] == 'Verb' and len(word[0]) > 1 and word[0] not in stopwords:
#             tmp.append(word[0]) 
#         elif word[1] == 'Adverb' and len(word[0]) > 1 and word[0] not in stopwords:
#             tmp.append(word[0])
#         elif word[1] == 'Adjective' and len(word[0]) > 1 and word[0] not in stopwords:
#             tmp.append(word[0])     
#     return tmp
    

df['okt_noun'] = df['han_text'].apply(lambda x : okt_noun(x))
# df['okt_verb'] = df['han_text'].apply(lambda x : okt_verb(x)) # verb에 동사, 형용사, 부사

df.to_csv('./nlp/words.csv')
