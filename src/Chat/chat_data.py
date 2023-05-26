import os
import sys
from pymongo import MongoClient
from src.Chat.Chat import *

client = MongoClient('mongodb+srv://sosschs9:1234@cluster0.fmfkril.mongodb.net/')
db = client['2023_GETIT_hackathon']
col_db = db['ChatList']

# DB 비어있는지 확인
def emptyChat():
    if getchatNumber() == 1:
        return True

# 새로운 대화 번호 가져오기
def getchatNumber():
    res = col_db.find().sort('_Chat__chatIdx', -1).limit(1)
    for i in res:
        return i['_Chat__chatIdx'] + 1
    return 1

# 대화 저장하기
def DB_addChatLog(chat: str, user):
    chat_id = getchatNumber()
    data = Chat(chat_id, chat, user)
    element = data.__dict__
    col_db.insert_one(element)

# 대화 불러오기
def getGpt(chatIdx: int):
    res = col_db.find_one({'_Chat__chatIdx': chatIdx})
    chat = Chat(res['_Chat__chatIdx'],res['_Chat__chatlog'])
    return chat

# 대화 삭제하기
def DB_deleteGpt(chatIdx: int):
    col_db.delete_one({'_Chat__chatIdx': chatIdx})

# 전체 대화 리스트 불러오기
def getAllChat():
    res = col_db.find().sort('_Chat__chatIdx', 1)
    ret = []
    for element in res:
        ret.append({'chat':element['_Chat__chatlog'], 'user':element['_Chat__user']})

    return ret

n=getchatNumber()
DB_deleteGpt(n-1)