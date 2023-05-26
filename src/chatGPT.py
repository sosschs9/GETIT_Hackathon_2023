import os
import openai

openai.api_key = ''

def getResponse(client_msg:str):
    messages_history = [
                {"role":"system", "content":""},
                {"role":"user", "content":""}
            ]
    messages_history.append({"role":"user", "content":client_msg})
    
    #요청
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_history
        )
    #응답 저장
    gpt_reply = completion.choices[0].message.content
    messages_history.append({"role":"assistant", "content":gpt_reply})

    return gpt_reply
    