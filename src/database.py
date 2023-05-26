import os
import sys
from pymongo import MongoClient
from src.Word import *

client = MongoClient('mongodb+srv://sosschs9:1234@cluster0.fmfkril.mongodb.net/')
db = client['2023_GETIT_hackathon']
col_db = db['WordList']

# 새로운 단어 번호 가져오기
def getWordNumber():
    res = col_db.find().sort('_Word__wordIdx', -1).limit(1)
    for i in res:
        print(i)
        return i['_Word__wordIdx'] + 1
    return 1

# 단어 저장하기
def DB_addWord(word: Word):
    element = word.__dict__
    col_db.insert_one(element)

# 단어 불러오기
def getWord(wordIdx: int):
    res = col_db.find_one({'_Word__wordIdx': wordIdx})
    word = Word(res['_Word__wordIdx'],res['_Word__word'], res['_Word__meaning'])
    return word

# 단어 삭제하기
def DB_deleteWord(wordIdx: int):
    col_db.delete_one({'_Word__wordIdx': wordIdx})

# 단어 수정하기
def DB_modifyWord(word: Word):
    DB_deleteWord(word.getWordID())
    DB_addWord(word)

# 전체 단어 리스트 불러오기
def getAllWord():
    res = col_db.find().sort('_Word__wordIdx', -1)
    ret = []
    for element in res:
        ret.append({'wordIdx': element['_Word__wordIdx'], 'word':element['_Word__word'], 'meaning':element['_Word__meaning']})

    return ret