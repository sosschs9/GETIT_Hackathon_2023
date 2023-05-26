import os
import sys

class Word():
    def __init__(self, wordIdx, word, meaning):
        self.__wordIdx = wordIdx
        self.__word = word
        self.__meaning = meaning
    
    def delete(self):
        pass
    def modify(self, word, meaning):
        self.__word = word
        self.__meaning = meaning
    def getWordIdx(self):
        return self.__wordIdx
    def getWord(self):
        return self.__word
    def getMeaning(self):
        return self.__meaning