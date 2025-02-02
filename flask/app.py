# /home/yokeshwaran/Desktop/flask/app.py
from flaskr import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)