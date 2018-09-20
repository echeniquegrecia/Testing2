from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'updating again 22'


if __name__ == '__main__':
    app.run()
