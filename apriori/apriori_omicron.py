#pip install tweepy==3.10.0
from apyori import apriori
import pandas as pd
import networkx as nx # pip install networkx=2.5
import matplotlib.pyplot as plt

# transactions = [
#     [], # 각 트윗 단어 리스트
#     []
# ]
transactions = []

df = pd.read_csv("./omicron.csv")

tmp = df['okt_noun'] # 각 행을 배열에 담기

# df['okt_noun'] 에 담겨있는 문자열을 list 자료형으로 변환
for t in tmp:
    transactions.append(t[2:-2])

i=0
for t in transactions:
    transactions[i] = t.split("', '")
    i += 1

for i in range(0, len(transactions)):
    tmp = []
    for word in transactions[i]:
        tmp.append(word)
    transactions[i] = tmp

########################################## 이제 transactions 에 각 트윗별 명사들 list형으로 저장됨

# apriori 수행

results = list(apriori(transactions,  # apriori 파라미터 조절
            min_support=20/5745,
            min_confidence=0.7,
            min_lift=30,
            max_length=2))

# results를 network_df 에 입력
columns = ['source', 'target', 'support']
network_df = pd.DataFrame(columns=columns)
for result in results:
    if len(result.items) == 2:
        items = [x for x in result.items]
        row = [items[0], items[1], result.support]
        series = pd.Series(row, index=network_df.columns)
        network_df = network_df.append(series, ignore_index=True)
##################################################################
 

# 모든 단어들 개수 세기
counter = {}
for nouns in transactions:
    for noun in nouns:
        try: counter[noun] += 1
        except: counter[noun] = 1

# 단어 개수 센 dict(@counter) 를 node_df에 넣기
columns = ['node', 'nodesize']
node_df = pd.DataFrame(columns=columns)
for key in counter.keys():
    row = [key, counter[key]]
    series = pd.Series(row, index=node_df.columns)
    node_df = node_df.append(series, ignore_index=True)

node_df = node_df[node_df['nodesize'] >= 1]
print(node_df.head())
#################################################################
# 아래에서 부터 graph 로 표현
plt.figure(figsize=(25,25))
G = nx.Graph()
    
for index, row in network_df.iterrows():
    G.add_node(row['source'], nodesize=1/(row['support']*5000)*1000)
    G.add_node(row['target'], nodesize=1/(row['support']*5000)*1000)
    G.add_weighted_edges_from([(row['source'], row['target'], row['support'])])



# 디자인 관련 파라미터
pos = nx.spring_layout(G, k=0.12, iterations=100)
sizes = [G.nodes[node]['nodesize']*20 for node in G]
nx.draw(G, pos=pos, node_color='#FFFF00',node_size=sizes)

nx.draw_networkx_labels(G, pos=pos, font_family='AppleGothic',font_weight='bold', font_size=13) # font 가 AppleGothic, Window는 'MalgunGothic' 사용

ax = plt.gca()
plt.show()
