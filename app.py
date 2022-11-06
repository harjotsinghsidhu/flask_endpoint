from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/') # http://www.mysite.com/
def home():
    return jsonify({'message': 'hello, world!'})


if __name__ == '__main__':
    app.run()
