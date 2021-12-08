#pip install tweepy==3.10.0
import re
from apyori import apriori
import pandas as pd
import networkx as nx # pip install networkx=2.5
import matplotlib.pyplot as plt

# transactions = [
#     [], # 각 트윗 단어 리스트
#     []
# ]
transactions = []
<<<<<<< HEAD

stop_word = ['위드', '코로나', '단계적', '단계', '일상', '회복', '백신', '패스', '진자']
df = pd.read_csv("./apriori/words2.csv") # 명사 나눈거 가져오기
=======
stop_word = ['위드', '코로나', '단계적', '단계', '일상', '회복', '백신', '패스', '진자', '오늘', '월일', '다음', '네이버', '출처', '뉴스']
df = pd.read_csv("./words2.csv") # 명사 나눈거 가져오기
>>>>>>> 715b7c0af50e5b63f073fe4653f62223919c186a
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

for i in range(0, len(transactions)):
    tmp = []
    for word in transactions[i]:
        if(word not in stop_word):
            tmp.append(word)
    transactions[i] = tmp

########################################## 이제 transactions 에 각 트윗별 명사들 list형으로 저장됨

# apriori 수행
results = list(apriori(transactions,  # apriori 파라미터 조절
<<<<<<< HEAD
            min_support=100/5745,
            min_confidence=0.5,
            min_lift=1.5,
=======
            min_support=20/5745,
            min_confidence=0.8,
            min_lift=3.0,
            # min_lift=0.8,
>>>>>>> 715b7c0af50e5b63f073fe4653f62223919c186a
            max_length=2))

# results를 network_df 에 입력
columns = ['source', 'target', 'support']
network_df = pd.DataFrame(columns=columns)
for result in results:
    # print(result)
    if len(result.items) == 2:
        items = [x for x in result.items]
        row = [items[0], items[1], result.support]
        series = pd.Series(row, index=network_df.columns)
        network_df = network_df.append(series, ignore_index=True)
##################################################################
print(network_df.head()) 

# 모든 단어들 개수 세기
counter = {}
for nouns in transactions:
    for noun in nouns:
        # if noun == '코로나' or noun == '위드' or noun == '일상' or noun =='단계' or noun == '회복' or noun == '백신' or noun == '패스': # 여기서 graph에 안나왔으면 하는 단어 추가 -> 이거 추가하면 에러떠서 일단 뺌
        #     continue
        try: counter[noun] += 1
        except: counter[noun] = 1

# 단어 개수 센 dict(@counter) 를 node_df에 넣기
columns = ['node', 'nodesize']
node_df = pd.DataFrame(columns=columns)
for key in counter.keys():
    row = [key, counter[key]]
    series = pd.Series(row, index=node_df.columns)
    node_df = node_df.append(series, ignore_index=True)

node_df = node_df[node_df['nodesize'] >= 20]  # node의 최소 frequency 조절
print(node_df.head())
#################################################################
# 아래에서 부터 graph 로 표현
plt.figure(figsize=(25,25))
G = nx.Graph()
# for index, row in node_df.iterrows():
    # G.add_node(row['node'], nodesize=row['nodesize'])
    
for index, row in network_df.iterrows():
    G.add_node(row['source'], nodesize=1/(row['support']*5000)*5000)
    G.add_node(row['target'], nodesize=1/(row['support']*5000)*5000)
    G.add_weighted_edges_from([(row['source'], row['target'], row['support'])])



# 디자인 관련 파라미터
pos = nx.spring_layout(G, k=0.6, iterations=50)
sizes = [G.nodes[node]['nodesize']*20 for node in G]
nx.draw(G, pos=pos, node_size=sizes)

nx.draw_networkx_labels(G, pos=pos, font_family='Malgun Gothic', font_size=15) # font 가 AppleGothic, Window는 'Malgun Gothic' 사용

ax = plt.gca()
plt.show()
