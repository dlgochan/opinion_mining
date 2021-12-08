# opinion_mining
트위터를 통해 위드코로나에 대한 여론을 수집하고 감정을 분석한다.


트위터 크롤링 : crawler/crawler.py > crawler/twitter.json

중복 제거 : crawler/twitter.json > crawler/rm_dup.py > crawler/re_dup.json

중복 제거된 tweet들이 저장된 json 형식 파일을 DataFrame으로 형변환 : crawler/re_dup.json > crawler/json2df.py > nlp/tweets.csv


자연어 정제(띄어쓰기, 오타?, 이모티콘, 영어 제거) : nlp/tweets.csv > nlp/text_cleaning.py > nlp/hanspell.csv


    정제된 트윗 text를 명사와 용언으로 분류 : nlp/hanspell.csv, nlp/korean_stopwords.txt > nlp/okt.py > nlp/words#.csv

    트윗에 나온 명사들 apriori로 관계 분석 : apriori/words2.csv > networkx package를 이용한 gui


자연어 정제 완료한 tweet들(hanspell.csv)로 텍스트 감정분석 API 진행한 결과 
    
    opm/sentiment.py > opm/sentiment_result.json
    

텍스트 감정분석 결과가 저장된 json 형식 파일에서 긍정/부정 tweet 판단 결과를 DataFrame으로 저장 
    
    opm/sentiment_to_DataFrame.py > opm/y_label.csv
    텍스트 감정분석 결과를 본래 저장된 opm/word2.csv에 merge


트윗에서 명사로 분리된 단어에 대해 TF-IDF 진행, 트윗에 대한 텍스트 감정 분석 결과로 학습하여 
긍정/부정적인 단어를 구별하기 위해 logistic regression 진행 
    
    > opm/classifier.py

    70%는 train, 30%는 test용으로 데이터셋을 분리
    성능 평가는 confusion matrix, accuracy, precision, recall, F1-score로 진행
    데이터 불균형 문제 발생, 긍정/부정적인 tweet의 비율을 1:1로 맞춰주기 위해 랜덤 샘플링 진행 후 성능 평가
    '위드코로나, 백신패스'에 대해 긍정/부정적 단어 20개씩 도출 







