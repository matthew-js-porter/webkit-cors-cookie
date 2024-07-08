import flask
from flask import Flask, render_template, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.set_cookie('cookie', 'cookie')
    return response


@app.route('/go')
def go():
    response = make_response()
    response.set_cookie('test', 'test')
    response.status = 302
    response.headers.add_header('Location', 'http://127.0.0.1:8080/there')
    return response


@app.route('/there')
def there():
    return redirect('http://localhost:8080/cookie')


@app.route('/cookie')
def cookie():
    print(flask.request.cookies.get('test'))
    print(flask.request.cookies.get('cookie'))
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
