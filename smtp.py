from flask import Flask, request, render_template_string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Gmail SMTP Server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # For TLS
SENDER_EMAIL = "yogesh441976@gmail.com"  # Replace with your email
APP_PASSWORD = "pgph akel ywqw xvyr"  # Replace with the generated app password

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish SMTP connection with Gmail
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.set_debuglevel(1)
                server.starttls()  # Secure the connection
                server.login(SENDER_EMAIL, APP_PASSWORD)
                server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
            return f"Email sent successfully to {recipient}!"
        except Exception as e:
            return f"Failed to send email: {e}"

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Send Email</title>
    </head>
    <body>
        <h2>Send Email via Gmail SMTP</h2>
        <form method="POST">
            <label for="recipient">Recipient:</label><br>
            <input type="email" id="recipient" name="recipient" required><br><br>

            <label for="subject">Subject:</label><br>
            <input type="text" id="subject" name="subject" required><br><br>

            <label for="body">Body:</label><br>
            <textarea id="body" name="body" required></textarea><br><br>

            <input type="submit" value="Send Email">
        </form>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
