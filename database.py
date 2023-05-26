import os
import sys
from pymongo import MongoClient
from Word import *

client = MongoClient('mongodb+srv://sosschs9:1234@cluster0.fmfkril.mongodb.net/')
db = client['2023_GETIT_hackathon']
col_db = db['WordList']

# 새로운 단어 번호 가져오기
def getWordNumber():
    res = col_db.find().sort('__Word__wordIdx', -1).limit(1)
    for i in res:
        return i['__Word__wordIdx'] + 1
    return 1

# 단어 저장하기
def DB_addWord(word: Word):
    return

# 단어 불러오기
def getWord(wordIdx: int):
    return

# 단어 삭제하기
def DB_deleteWord(wordIdx: int):
    return

# 단어 수정하기
def DB_modifyWord(word: Word):
    return

# 전체 단어 리스트 불러오기
def getAllWord():
    return
