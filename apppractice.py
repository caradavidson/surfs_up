from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

# make sure vscode is in right environment on bottom, I am currently in 'python data'

