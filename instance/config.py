from dotenv import load_dotenv
import os

load_dotenv()

# Database configuration
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_DB = os.getenv('MYSQL_DB')

SECRET_KEY = os.getenv('SECRET_KEY')

#reCAPTCHA keys
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')

# Optional parameters
# RECAPTCHA_PARAMETERS = {'hl': 'en'}  # Set language to English
# RECAPTCHA_DATA_ATTRS = {'theme': 'light'} 

#smtp login credential

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_EMAIL = os.getenv('SMTP_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
SMTP_RECPT = os.getenv('SMTP_RECPT')

#GEMINI API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

#AI MODEL
TEXT_GENERATE_AI_MODEL = os.getenv('TEXT_GENERATE_AI_MODEL')