# -*- coding: utf-8 -*-
import os
import openai
import json
from flask import Flask, request, render_template

def Chatgpt_api():
    openai.api_key = ""

    app = Flask(__name__)
    # CORS(app)
    @app.route('/')
    @app.route('/diction_post', methods=['GET','POST'])
    def diction_post():
        if request.method =='POST':
            usermessages = request.form['input_name']# <- 에러나면 input_name 지워보기
            #usermessages = request.form
            usermessages = str(usermessages)
            print(usermessages)
            messages_history = [
                        {"role":"system", "content":"Analyze the next sentence and recommend a 'gesture' that the speaker of the sentence would do. As a result of the gesture recommendations in the sentence, You can choose one from the list. list=['wave your hand', 'hit the person next to you', 'kiss you', 'hurray', 'cover your face with your hands'.] For example, if I send the sentence, '권민철: 오늘 알바비 들어왔다' you can recommend the action of 'hurray'. Now, analyze the sentence."},
                        {"role":"user", "content":"Analyze the next sentence and recommend a 'gesture' that the speaker of the sentence would do. As a result of the gesture recommendations in the sentence, You can choose one from the list. list=['wave your hand', 'hit the person next to you', 'kiss you', 'hurray', 'cover your face with your hands'.] For example, if I send the sentence, '권민철: 오늘 알바비 들어왔다' you can recommend the action of 'hurray'. Now, analyze the sentence."}
                    ]
            messages_history.append({"role":"user", "content":usermessages})
            #print(messages_history)
            
            #요청
            completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages_history
                )

            #응답 저장
            gpt_reply = completion.choices[0].message.content
            print(gpt_reply)
            #messages_history.append({"role":"assistant", "content":gpt_reply})
            #print(messages_history)
        
        return gpt_reply
    
def requestion():
