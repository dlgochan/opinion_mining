from apyori import apriori

# transactions = [
#     [], # 각 트윗 단어 리스트
#     []
# ]
transactions = []
df = pd.read_csv(".csv") # 명사 나눈거 가져오기
transactions.append() # 각 행을 배열에 담기


results = list(apriori(transactions))
for result in results:
    print(result)

list(apriori(transactions,
            min_support=0.5,
            min_confidence=0.6,
            min_lift=1.0,
            max_length=2))