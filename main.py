from flask import Flask
from deep_translator import MyMemoryTranslator as ts

app = Flask(__name__)


@app.route("/<text>")
def translate(text):
    translated = ts(source='zh-CN', target='en-US').translate(text)
    return translated
