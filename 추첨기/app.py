from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
출처: https://wings2pc.tistory.com/entry/웹-앱프로그래밍-파이썬-플라스크Python-Flask-설치-및-웹-애플리케이션Web-Application-시작 [Wings on PC:티스토리]