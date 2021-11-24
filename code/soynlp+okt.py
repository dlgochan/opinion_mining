from soynlp.word import WordExtractor
from soynlp.tokenizer import MaxScoreTokenizer
from soynlp import DoublespaceLineCorpus
import json
from konlpy.tag import Okt

# soynlp로 단어 분류하기
corpus = DoublespaceLineCorpus("hanspell.json")

word_extractor = WordExtractor()
word_extractor.train(corpus)

word_score = word_extractor.extract()

scores = {word:score.cohesion_forward for word, score in word_score.items()}

maxscore_tokenizer = MaxScoreTokenizer(scores=scores)


# soynlp에 okt 품사 분류
f_input = open("hanspell.json", mode="r")
f_output = open("soynlp+okt.json", mode = "w")

str = []
tweets = []

str = f_input.readlines() 

for j in str:
    tweets.append(json.loads(j)) # json -> dict

soynlp_words = []
for j in tweets:
    for w in maxscore_tokenizer.tokenize(j['text']):
        soynlp_words.append(w)
    
okt = Okt()
for words in soynlp_words:
    # 명사나 형용사만 추출
    for word in okt.pos(words): 
        if word[1] == 'Noun':
            tmp = {'명사' : word[0]}
            tmp2 = json.dumps(tmp)
            f_output.write(tmp2)
            f_output.write('\n')
        elif word[1] == 'Adjective':
            tmp = {'형용사' : word[0]}
            tmp2 = json.dumps(tmp)
            f_output.write(tmp2)
            f_output.write('\n')
