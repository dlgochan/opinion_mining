import pandas as pd
import numpy as np
import sys
import requests
import json

f = open("opm\sentiment_result.json", mode='w',encoding='UTF-8')     # 쓰기 모드
result = []

# 감정분석 API 연동
# 수빈 계정으로 업데이트
client_id = "lezo3ogzqg"
client_secret = "llsiREmWUFRxHcPXsONaf17WqnP6aieO01FnbXst"
url="https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}

#csv 파일 불러오기
df = pd.read_csv("./nlp/omicron_hanspell.csv")
count = len(df)

# text 한 줄씩 읽어서 API 실행
hantext= df['han_text'].values.tolist()

for num in hantext:
    content = num
    data = {
        "content": content
    }
    print(json.dumps(data, indent=4, sort_keys=True))
    response = requests.post(url, data=json.dumps(data), headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        result = response.text
        f.write(result)
        f.write('\n')
    else:
        print("Error : " + response.text)





