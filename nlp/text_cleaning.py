# -*- conding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from hanspell import spell_checker

def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글 정규표현식
    result = hangul.sub('', text)
    return result

# 크롤링 데이터 읽기
df = pd.read_csv("tweets.csv")


columns = []
df2 = pd.DataFrame(columns=columns)
df2['ko_text'] = df['text'].apply(lambda x : text_cleaning(x)) # tweet_text는 받은 데이터 보고 수정하기

print(df2.head())

# ============================ 여기까지 한글 추출

def text_hanspell(text):
    spelled_text = spell_checker.check(text) # 맞춤법 교정
    return spelled_text.checked
    

df3 = pd.DataFrame(columns=columns)
df3['han_text'] = df2['ko_text'].head().apply(lambda x : text_hanspell(x))

print(df3.head())
    
