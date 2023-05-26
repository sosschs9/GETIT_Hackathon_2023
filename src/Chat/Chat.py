import os
import sys

class Chat():
    def __init__(self, chatIdx, chatlog, user):
        self.__chatIdx = chatIdx
        self.__chatlog = chatlog
        self.__user = user
    
    def delete(self):
        pass
    def getChatIdx(self):
        return self.__chatIdx
    def getChatLog(self):
        return self.__chatlog
    def getUser(self):
        return self.__user
    
