from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return "Hello World! 湛霄禹"
app.run(port='8000')


