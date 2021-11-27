from sklearn.model_selection import train_text_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

y=df['y']
x_train, x_test, y_train, y_test = train_text_split(X,y,test_size=0.30)
print(x_train.shape)
print(x_test.shape)

# �� �н�
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

#���� ��
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision: %.3f" % precision_score(y_test, y_pred))
print("Recall: %.3f" % recall_score(y_test, y_pred))
print("F1: %.3f" % f1_score(y_test, y_pred))


#Confusion Matrix ���
confmat= confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

#y�� 0�� 1�� �󸶳� ������ �ִ��� ���
print(df['y'].value_counts())

#1:1 ������ ���� ���ø� ����
positive_random_idx = df[df['y']==1].sample(50,random_state=30).index.tolist()
negative_random_idx = df[df['y']==0].sample(50,random_state=30).index.tolist()

#���� �����ͷ� �����ͼ��� ����
random_idx = positive_random_idx+negative_random_idx
sample_X=X[random_idx,:]
y= df['y'][random_idx]
x_train, x_test, y_train, y_test = train_text_split(sample_X, y, test_size = 0.30)
print(x_train.shape)
print(x_test.shape)

#�ٽ� �� �н�
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

#���� ��
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision: %.3f" % precision_score(y_test, y_pred))
print("Recall: %.3f" % recall_score(y_test, y_pred))
print("F1: %.3f" % f1_score(y_test, y_pred))

#Confusion Matrix ���
confmat= confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

#�н��� ���� ����� ����Ͽ� ��ó ������� Ȯ��
plt.rcParms['figure.figsize']=[10,8]
plt.bar(range(len(lr.coef_[0])), lr.coef_[0])
print(sorted(((value,index) for index, value in enumerate(lr.coef_[0])), reverse=True)[:5])
print(sorted(((value,index) for index, value in enumerate(lr.coef_[0])), reverse=True)[-5:])

#ȸ�� ���� ����� ���� ������ ����
coef_pos_index = sorted(((value, index) for index, value in enumerate(lr.coef_[0])),reverse=True)

#ȸ�� ���� ����� index_vec�� �����Ͽ� � ���¼����� ����� �� �ְ� ��
invert_index_vectorizer = {v: k for k, v in index_vectorizer.vocabulary_.items()}

#����� ���� ������ ��ó�� ���¼Ҹ� ������ ����� ���
#����� ���� feature�� ���� �������� ������ �ִ� ���¼�
print(str(invert_index_vectorizer)[:100]+'..')

for coef in coef_pos_index[:20]:
    print(invert_index_vectorizer[coef[1]],coef[0])