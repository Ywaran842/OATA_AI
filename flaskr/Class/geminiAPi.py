from flask import current_app

class gemini_API_MODEL:

    @staticmethod
    def get_gemini_api_key():
        return current_app.config['GEMINI_API_KEY']
    
    @staticmethod
    def get_text_generate_ai_model():
        return current_app.config['TEXT_GENERATE_AI_MODEL']