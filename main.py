import os

from flask import Flask, request
import argparse
from deep_translator import GoogleTranslator as ts

app = Flask(__name__)

# 使用 argparse 解析命令行参数
parser = argparse.ArgumentParser(description='Flask App with Proxy Argument')
parser.add_argument('--proxy', help='Specify the proxy address')
args = parser.parse_args()

PROXY = args.proxy


@app.route("/")
def home():
    return "This service is alive."


@app.route("/translate", methods=['GET'])
def translate():
    text = request.args.get('text')
    source = request.args.get('from', 'auto')
    to = request.args.get('to')
    translated = ts(source=source, target=to, proxies={"http": PROXY, 'https': PROXY} if PROXY else None).translate(text)
    return translated


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081")
