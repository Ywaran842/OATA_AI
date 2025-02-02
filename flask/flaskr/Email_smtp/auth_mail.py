from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP, SMTPException
from flaskr.error.writeerror import write_error_to_file
from flask import current_app

class mail:
    
    @staticmethod
    def mail(subject, message):
        msg = MIMEMultipart()
        msg['From'] = current_app.config['SMTP_EMAIL']
        msg['To'] = current_app.config['SMTP_RECPT']
        msg['Subject'] = subject

        #body for mail
        msg.attach(MIMEText(message, 'plain'))

        #smtp with mail server
        with SMTP(current_app.config['SMTP_SERVER'], current_app.config['SMTP_PORT']) as smtp:
            smtp.starttls()
            smtp.login(current_app.config['SMTP_EMAIL'], current_app.config['APP_PASSWORD'])
            smtp.sendmail(current_app.config['SMTP_EMAIL'], current_app.config['SMTP_RECPT'], msg.as_string())
            