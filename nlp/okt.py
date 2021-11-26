# -*- conding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt

okt = Okt()

df = pd.read_csv("hanspell.csv")
columns = []
df2 = pd.DataFrame(columns=columns)

def okt_noun(text):
    tmp = []
    words = okt.pos(text)
    for word in words: 
        if word[1] == 'Noun':
            tmp.append(word[0])
    return tmp

def okt_verb(text):
    tmp = []
    words = okt.pos(text)
    for word in words: 
        if word[1] == 'Verb':
            tmp.append(word[0]) 
        elif word[1] == 'Adverb':
            tmp.append(word[0])
        elif word[1] == 'Adjective':
            tmp.append(word[0])     
    return tmp
    
    
df2['okt_noun'] = df['han_text'].apply(lambda x : okt_noun(x))
df2['okt_verb'] = df['han_text'].apply(lambda x : okt_verb(x)) # verb에 동사, 형용사, 부사

df2.to_csv('words.csv')
 