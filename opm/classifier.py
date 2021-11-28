from sklearn.model_selection import train_text_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
import pandas as pd
from konlpy.tag import Okt


df = pd.read_csv("C:/Users/wngus/Documents/GitHub/opinion_mining/opm/words2.csv")


# corpus index 생성
index_vectorizer = CountVectorizer() # 토큰화, 벡터화를 같이 해줌
X = index_vectorizer.fit_transform(df['okt_verb']) # 토큰화 이미 해놨으니까 그냥 해놓은거 넣기만 하면 됨
# (5744, 7269) :  7269의 feature를 가진 5744개의 학습 데이터 셋 

print(X.shape)
print(X[1])
print('===================================================')

# TF-IDF
tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)

print(X.shape)
print(X[1])

y=df['y']
x_train, x_test, y_train, y_test = train_text_split(X,y,test_size=0.30)
print(x_train.shape)
print(x_test.shape)

# 모델 학습
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

#성능 평가
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision: %.3f" % precision_score(y_test, y_pred))
print("Recall: %.3f" % recall_score(y_test, y_pred))
print("F1: %.3f" % f1_score(y_test, y_pred))


#Confusion Matrix 출력
confmat= confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

#y가 0과 1을 얼마나 가지고 있는지 출력
print(df['y'].value_counts())

#1:1 비율로 랜덤 샘플링 수행
positive_random_idx = df[df['y']==1].sample(50,random_state=30).index.tolist()
negative_random_idx = df[df['y']==0].sample(50,random_state=30).index.tolist()

#랜덤 데이터로 데이터셋을 나눔
random_idx = positive_random_idx+negative_random_idx
sample_X=X[random_idx,:]
y= df['y'][random_idx]
x_train, x_test, y_train, y_test = train_text_split(sample_X, y, test_size = 0.30)
print(x_train.shape)
print(x_test.shape)

#다시 모델 학습
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

#성능 평가
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision: %.3f" % precision_score(y_test, y_pred))
print("Recall: %.3f" % recall_score(y_test, y_pred))
print("F1: %.3f" % f1_score(y_test, y_pred))

#Confusion Matrix 출력
confmat= confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

#학습한 모델의 계수를 출력하여 피처 영향력을 확인
plt.rcParms['figure.figsize']=[10,8]
plt.bar(range(len(lr.coef_[0])), lr.coef_[0])
print(sorted(((value,index) for index, value in enumerate(lr.coef_[0])), reverse=True)[:5])
print(sorted(((value,index) for index, value in enumerate(lr.coef_[0])), reverse=True)[-5:])

#회귀 모델의 계수를 높은 순으로 정렬
coef_pos_index = sorted(((value, index) for index, value in enumerate(lr.coef_[0])),reverse=True)

#회귀 모델의 계수를 index_vec에 맵핑하여 어떤 형태소인지 출력할 수 있게 함
invert_index_vectorizer = {v: k for k, v in index_vectorizer.vocabulary_.items()}

#계수가 높은 순으로 피처에 형태소를 맵핑한 결과를 출력
#계수가 높은 feature는 립에 긍정적인 영향을 주는 형태소
print(str(invert_index_vectorizer)[:100]+'..')

for coef in coef_pos_index[:20]:
    print(invert_index_vectorizer[coef[1]],coef[0])