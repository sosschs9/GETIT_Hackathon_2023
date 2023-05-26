# Client ID: Q5koRFqSPEdp8nX4ZZpq
# Client Secret: bMW9tjiT2c
import os
import sys
import requests

client_id = "Q5koRFqSPEdp8nX4ZZpq"
client_secret = "bMW9tjiT2c"
url = "https://openapi.naver.com/v1/papago/n2mt"

def translate(src, target, data):
    req_header = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    req_param = {"source":src, "target":target, "text":data}

    res = requests.post(url,headers=req_header, data=req_param)
    if res.ok:
        #print(type(res.text),res.text)
        #print(type(res.json()),res.json())
        trans_txt=res.json()['message']['result']['translatedText']
        return trans_txt
    else:
        print('error code', res.status_code)
        return -1
    
