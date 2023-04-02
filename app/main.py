from flask import Flask

app = Flask(__name__)


@app.get('/')
def main_page():
    return "<h1>Hello, World!</h1>"
