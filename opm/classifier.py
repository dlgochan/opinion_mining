#-*- coding: utf-8, cp949 -*-
#-*- Encoding: UTF-8 -*-#
#%%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("./words2.csv", encoding='cp949')


# corpus index ����
index_vectorizer = CountVectorizer() # ��ūȭ, ����ȭ�� ���� ����
X = index_vectorizer.fit_transform(df['okt_noun']) # ��ūȭ �̹� �س����ϱ� �׳� �س����� �ֱ⸸ �ϸ� ��
# (5744, 7269) :  7269�� feature�� ���� 5744���� �н� ������ �� 

print(X.shape)
print(X[1])
print('===================================================')

# TF-IDF
tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)
print('tf-idf result')
print(X.shape)
print(X[1])

#X: tf-idf ó�� �� �ܾ� ���, ������, ���̺� ���� ����, test�� 30%�� ���
#test�� �����ͼ� �и�
print("random sampling X- train_test label")
y=df['y']
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.30, random_state=30)
print(x_train.shape)
print(x_test.shape)

# �� �н�
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

#���� ��
print("random sampling X - learning result")
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision: %.3f" % precision_score(y_test, y_pred))
print("Recall: %.3f" % recall_score(y_test, y_pred))
print("F1: %.3f" % f1_score(y_test, y_pred))


#Confusion Matrix ���
print("random sampling X - Confusion_matrix")
confmat= confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

#y�� 0�� 1�� �󸶳� ������ �ִ��� ���(Ŭ���� �ұ��� ���� �ذ��� ����)
print("random sampling X - number of y on 0, 1")
print(df['y'].value_counts())



print('===================================================')
#1:1 ������ ���� ���ø� ����
# y�� 1,2�� ���� �� 50���� ���Ƿ� �����ؼ� ������ ������
positive_random_idx = df[df['y']==1].sample(1300,random_state=30).index.tolist()
negative_random_idx = df[df['y']==0].sample(1300,random_state=30).index.tolist()

#���� �����ͷ� �����ͼ��� ����
# test�� 30%, train 70%
print("random sampling O - train_test label")
random_idx = positive_random_idx+negative_random_idx
sample_X=X[random_idx,:]
y= df['y'][random_idx]
x_train, x_test, y_train, y_test = train_test_split(sample_X, y, test_size = 0.30,random_state=30)
print(x_train.shape)
print(x_test.shape)

#�����͸� �ٽ� ������ �� �� �н� ������
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

#���� ��
print("random sampling O - learning result")
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision: %.3f" % precision_score(y_test, y_pred))
print("Recall: %.3f" % recall_score(y_test, y_pred))
print("F1: %.3f" % f1_score(y_test, y_pred))

#Confusion Matrix ���
print("random sampling O - Confusion_matrix")
confmat= confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

#�н��� ���� ����� ����Ͽ� ��ó ������� Ȯ��
# ����� �͵��� Ʈ������ �������̶�� �ǴܵǴ� �ܾ�, ������ Ʈ������ �������̶�� �ǴܵǴ� �ܾ��� �Ǵ���.
plt.rcParams['figure.figsize']=[10,8]
plt.bar(range(len(lr.coef_[0])), lr.coef_[0])
print(sorted(((value,index) for index, value in enumerate(lr.coef_[0])), reverse=True)[:5])
print(sorted(((value,index) for index, value in enumerate(lr.coef_[0])), reverse=True)[-5:])

#ȸ�� ���� ����� ���� ������ ����
# ���� �ܾ�� ���� �ܾ ����ϱ� ���� ����� �������� �ܾ �����ϰ�, ���ĵ� ���͸� index_vectorizer ��ü�� �ٽ� ��� ����
coef_pos_index = sorted(((value, index) for index, value in enumerate(lr.coef_[0])),reverse=True)

#ȸ�� ���� ����� index_vec�� �����Ͽ� � ���¼����� ����� �� �ְ� ��
invert_index_vectorizer = {v: k for k, v in index_vectorizer.vocabulary_.items()}

#����� ���� ������ ��ó�� ���¼Ҹ� ������ ����� ���
print(str(invert_index_vectorizer)[:100]+'..')

print("Positive top 20")
#����� ���� feature�� ���� �������� ������ �ִ� ���¼�
i=0
for coef in coef_pos_index[:40]:
    print(i,invert_index_vectorizer[coef[1]],coef[0])
    i+=1
print("================================================================")

print("Negative top 20==========")
i=0
#����� ���� feature�� ���� �������� ������ �ִ� ���¼�
for coef in coef_pos_index[-40:]:
    print(i, invert_index_vectorizer[coef[1]],coef[0])
    i+=1
# %%
