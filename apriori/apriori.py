import re
from apyori import apriori
import pandas as pd

# transactions = [
#     [], # 각 트윗 단어 리스트
#     []
# ]
transactions = []
df = pd.read_csv("./words2.csv") # 명사 나눈거 가져오기
tmp = df['okt_noun'] # 각 행을 배열에 담기

# df['okt_noun'] 에 담겨있는 문자열을 list 자료형으로 변환
for t in tmp:
    # print(t[2:-1])
    transactions.append(t[2:-2])

i=0
for t in transactions:
    transactions[i] = t.split("', '")
    i += 1
    # print(t[0])
################################################## 이제 transactions 에 각 트윗별 명사들 list형으로 저장됨

# for transaction in transactions:
#     print(transaction)
#     for term in transaction:
#         print(term)

results = list(apriori(transactions,
            min_support=0.001,
            min_confidence=0.1,
            # min_lift=1.0,
            max_length=2))
for result in results:
    print(result)
#     if

