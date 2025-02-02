from flask import current_app
import pymysql
from getConnection import Database
import google.generativeai as genai
from geminiAPi import gemini_API_MODEL

class genimichat:

    #Get the user chat History
    @staticmethod
    def get_chat(userid):
        connection = Database.getConnection()
        cursor = connection.cursor()
        cursor.execute('select * from chat where user_id = %s', userid)
        chat = cursor.fetchall()
        return chat

    #generate a responce for text.
    @staticmethod
    def responce_with_text(message, userid):
        chat = chat.get_chat(userid)
        if chat is not None:
            history = []
            for i in chat:
                history.append({"message": "user", "parts": i["user_chat"]})
                history.append({"message": "model", "parts": i["ai_chat"]})
        genai.configure(api_key= gemini_API_MODEL.get_gemini_api_key())
        model = genai.GenerativeModel(model=gemini_API_MODEL.get_text_generate_ai_model())
        chat = model.start_chat(history)
        responce = chat.send_message(message)
        return responce

        
