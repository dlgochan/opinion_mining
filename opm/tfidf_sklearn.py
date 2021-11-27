from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from konlpy.tag import Okt


df = pd.read_csv("../nlp/words2.csv")

# corpus index 생성
index_vectorizer = CountVectorizer() # 토큰화, 벡터화를 같이 해줌
X = index_vectorizer.fit_transform(df['okt_verb']) # 토큰화 이미 해놨으니까 그냥 해놓은거 넣기만 하면 됨
# (5744, 7269) :  7269의 feature를 가진 5744개의 학습 데이터 셋 

# print(X.shape)
# print(X[1])
# print('===================================================')

# TF-IDF
tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)

# print(X.shape)
# print(X[1])

