from flask import Flask, render_template, request
from src.papago import *
from src.chatGPT import *
from src.Word import *
from src.database import *

app = Flask(__name__)

cnt = 0
client_msg = ""
question_list = []

# 채팅 페이지
@app.route('/',  methods=['GET', 'POST'])
def chat():
    global cnt, client_msg, question_list
    if request.method == 'GET':
        return render_template("chat.html")
    if request.method == 'POST':
        data = request.form['question']
        client_msg += data + ', '
        cnt = (cnt+1) % 3
        if (cnt == 1):
            question_list = []
            question_list.append('그 단어의 품사는 무엇인가요?')
            return render_template("chat.html", question_list = question_list)
        elif (cnt == 2):
            question_list.append('그 단어를 사용하는 상황은 무엇인가요?')
            return render_template("chat.html", question_list = question_list)
        elif (cnt == 0):
            client_msg += " 앞 설명에 부합하는 단어가 뭐야?"
            translate_txt = translate('ko', 'ja', client_msg)
            translate_txt = translate('ja', 'en', translate_txt)
            gpt_response = getResponse(translate_txt) # 사용자 질문 내용을 gpt에게 전달함.
            gpt_response = translate('en', 'ko', gpt_response)
            return render_template("chat.html", question_list = question_list, response = gpt_response)

# 설정 페이지
@app.route('/setting')
def setting():
    return render_template("setting.html")

if __name__ == '__main__':
    app.run()