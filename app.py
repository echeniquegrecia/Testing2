from flask import Flask

app = Flask(__name__)
test = "dd"

@app.route('/')
def hello_world():
    return 'updating again 22'

@app.route('/testing1')
def testing1():
    return 'testing1'

@app.route('/testing2')
def testing2():
    return 'testing2'


if __name__ == '__main__':
    app.run()
