from flask import Flask, render_template, request

app = Flask(__name__)

# 채팅 페이지
@app.route('/')
def chat():
    return render_template("chat.html")

# 사용자 입력 -> 


# 설정 페이지
@app.route('/setting')
def setting():
    return render_template("setting.html")
