from flask import Flask, render_template, request
from papago import *
import openai

app = Flask(__name__)

# 채팅 페이지
@app.route('/',  methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template("chat.html")
    if request.method == 'POST':
        data = request.form['question']
        translate_txt = translate('ko', 'en', data)
        return render_template("chat.html", response = translate_txt)


# 설정 페이지
@app.route('/setting')
def setting():
    return render_template("setting.html")

if __name__ == '__main__':
    app.run()