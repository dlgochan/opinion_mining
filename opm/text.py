#!/usr/bin/env python3
#-*- codig: utf-8 -*-

import sys
import requests
import json

client_id = "go0qt8vm6i"
client_secret = "6zy44GwDgpAROILjgVuhBXFnfAZmuRzFHJ1e5etS"
url="https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}

content = "싸늘하다. 가슴에 비수가 날아와 꽂힌다."
data = {
  "content": content
}

print(json.dumps(data, indent=4, sort_keys=True))
response = requests.post(url, data=json.dumps(data), headers=headers)
rescode = response.status_code

if(rescode == 200):
    text = response.text
    print(text)
else:
    print("Error : " + response.text)

print("Hello")
