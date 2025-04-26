import google.generativeai as genai
API_KEY= "AIzaSyAKnjEBoVCidIqHZIyrEPe4ZTipqFH6gIU"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-2.0-flash')
chat=model.start_chat()
while True:
    user_input=input('You: ')
    if user_input=="exit":
        print('Chat Terminated')
        break
    else:
        response=chat.send_message(user_input)
        print("Gemini: ",response.text)