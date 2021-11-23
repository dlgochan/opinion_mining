from soynlp.word import WordExtractor
from soynlp.tokenizer import MaxScoreTokenizer
from soynlp import DoublespaceLineCorpus

corpus = DoublespaceLineCorpus("twitter.txt")

word_extractor = WordExtractor()
word_extractor.train(corpus)

word_score = word_extractor.extract()

scores = {word:score.cohesion_forward for word, score in word_score.items()}

maxscore_tokenizer = MaxScoreTokenizer(scores=scores)
print(maxscore_tokenizer.tokenize('''수업으로고3보냈어'''))

