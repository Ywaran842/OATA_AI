from flask import Flask
import logging
from logging.handlers import SMTPHandler

app = Flask(__name__)

# Configure the app's SMTPHandler for logging
mail_handler = SMTPHandler(
    mailhost='smtp.gmail.com',  # Replace with your SMTP server address
    fromaddr='your-ema',  # Replace with your email
    toaddrs=['admin@example.com'],  # Replace with admin's email
    subject='Application Error'
)

# Set the logging level to ERROR
mail_handler.setLevel(logging.ERROR)

# Set the format for the log email
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

# If the app is not in debug mode, add the handler
if not app.debug:
    app.logger.addHandler(mail_handler)

@app.route('/')
def home():
    app.logger.error("An error occurred")  # Example error to test logging
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for testing error logging
