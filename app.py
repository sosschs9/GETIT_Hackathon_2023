from flask import Flask, render_template, request, redirect
from src.papago import *
from src.chatGPT import *
from src.Word.Word import *
from src.Word.word_data import *
from src.Chat.Chat import *
from src.Chat.chat_data import *

app = Flask(__name__)

cnt = 0
client_msg = ""
question_list = []
chat_list = []

# 처음 로딩페이지
@app.route('/')
def loading():
    return render_template("loading.html")

# 채팅 페이지
@app.route('/chat',  methods=['GET', 'POST'])
def chat():
    global cnt, client_msg, chat_list

    if request.method == 'GET':
        if emptyChat() == True:
            DB_addChatLog("안녕하세요! 궁금한 단어에 대해 입력해주세요", "GPT")
        chat_list = getAllChat()
        return render_template("chat.html", chat_list=chat_list)
    
    if request.method == 'POST':
        data = request.form['user_input']
        DB_addChatLog(data, "USER")

        client_msg += data + ', '
        cnt = (cnt+1) % 3
        if (cnt == 1):
            DB_addChatLog("그 단어의 품사는 무엇인가요?", "GPT")
        elif (cnt == 2):
            DB_addChatLog("그 단어를 사용하는 상황은 무엇인가요?", "GPT")
        elif (cnt == 0):
            client_msg += " 앞 설명에 부합하는 단어가 뭐야?그리고 답변해줄 때 \"\"<- 이 기호 쓰지말고 그 단어만 얘기해줘"
            # translate_txt = translate('ko', 'ja', client_msg)
            # translate_txt = translate('ja', 'en', translate_txt)
            gpt_response = getResponse(client_msg) # 사용자 질문 내용을 gpt에게 전달함.
            DB_addChatLog(gpt_response, "GPT")
            DB_addChatLog("안녕하세요! 궁금한 단어에 대해 입력해주세요", "GPT")
            # gpt_response = translate('en', 'ko', gpt_response)
        
        chat_list = getAllChat()
        return render_template("chat.html", chat_list=chat_list)

#채팅 페이지 채팅 아이콘
@app.route('/delete',methods=['GET','POST'])
def delete():
    my_data=request.form['my_data']
    n=getchatNumber()
    while n!=1:
        DB_deleteGpt(n-1)
        n=getchatNumber()
    if emptyChat() == True:
        DB_addChatLog("안녕하세요! 궁금한 단어에 대해 입력해주세요", "GPT")
    chat_list = getAllChat()
    return render_template("chat.html", chat_list=chat_list)

# 단어장 페이지
@app.route('/wordlist', methods=['GET', 'POST'])
def wordlist():
    word_list = getAllWord()
    return render_template('wordlist.html', word_list = word_list)

# 새로운 단어 추가 페이지
@app.route('/record_word', methods=['GET', 'POST'])
def record_word():
    if request.method == 'GET':
        return render_template('record_word.html')
    if request.method == 'POST':
        word = request.form['word']
        meaning = request.form['meaning']
        wordIdx = getWordNumber()
        new_word = Word(wordIdx, word, meaning)
        DB_addWord(new_word)
        return redirect('/wordlist')

# 설정 페이지
@app.route('/setting')
def setting():
    return render_template("settings.html")

# 카드뉴스 페이지
@app.route('/news')
def news():
    return render_template("news.html")



if __name__ == '__main__':
    app.run()