# opinion_mining
트위터를 통해 위드코로나에 대한 여론을 수집하고 감정을 분석한다.


트위터 크롤링 : crawler/crawler.py > crawler/twitter.json

중복 제거 : crawler/twitter.json > crawler/rm_dup.py > crawler/re_dup.json

중복 제거된 tweet들이 저장된 json 형식 파일을 DataFrame으로 형변환 : crawler/re_dup.json > crawler/json2df.py > nlp/tweets.csv


자연어 정제(띄어쓰기, 오타?, 이모티콘, 영어 제거) : nlp/tweets.csv > nlp/text_cleaning.py > nlp/hanspell.csv


    정제된 트윗 text를 명사와 용언으로 분류 : nlp/hanspell.csv, nlp/korean_stopwords.txt > nlp/okt.py > nlp/words#.csv

    트윗에 나온 명사들 apriori로 관계 분석 : apriori/words2.csv > networkx package를 이용한 gui







