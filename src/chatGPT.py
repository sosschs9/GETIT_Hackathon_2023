import os
import openai

openai.api_key = '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'

def getResponse(client_msg:str):
    messages_history = [
                {"role":"system", "content":"Analyze the next sentence and recommend a 'gesture' that the speaker of the sentence would do. As a result of the gesture recommendations in the sentence, You can choose one from the list. list=['wave your hand', 'hit the person next to you', 'kiss you', 'hurray', 'cover your face with your hands'.] For example, if I send the sentence, '권민철: 오늘 알바비 들어왔다' you can recommend the action of 'hurray'. Now, analyze the sentence."},
                {"role":"user", "content":"Analyze the next sentence and recommend a 'gesture' that the speaker of the sentence would do. As a result of the gesture recommendations in the sentence, You can choose one from the list. list=['wave your hand', 'hit the person next to you', 'kiss you', 'hurray', 'cover your face with your hands'.] For example, if I send the sentence, '권민철: 오늘 알바비 들어왔다' you can recommend the action of 'hurray'. Now, analyze the sentence."}
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
    