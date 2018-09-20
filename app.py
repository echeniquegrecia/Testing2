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

@app.route('/testing3')
def testing3():
    return 'testing3'

@app.route('/testing4')
def testing4():
    return 'testing4'

@app.route('/testing5')
def testing5():
    return 'testing5'



if __name__ == '__main__':
    app.run()
