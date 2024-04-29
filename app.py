from flask import Flask,make_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'hellow world'
if __name__ == '__main__':
    app.run()