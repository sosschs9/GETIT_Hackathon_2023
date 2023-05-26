import os
import sys

class Word():
    def __init__(self, wordID, word, meaning):
        self.__wordID = wordID
        self.__word = word
        self.__meaning = meaning
    
    def delete(self):
        pass
    def modify(self, word, meaning):
        self.__word = word
        self.__meaning = meaning
    def getWordID(self):
        return self.__wordID
