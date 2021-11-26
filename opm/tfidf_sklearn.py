from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TFidfTransformer

index_vectorizer = CountVectorizer(tokenizer = lambda x: get_pos(x))
X = index_vectorizer.fit_transform(df['ko_text'].tolist())
print(X.shape)

print(str(index_vectorizer.vocabulary_)[:100]+"..")
print(df['ko_text'][0])
print(X[0])

tfidf_vectorizer = TFidfTransformer()
X = tfidf_vectorizer.fit_transform(X)

print(X.shape)
print(X[0])
