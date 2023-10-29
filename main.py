from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api():
    data = {'message': 'This is a sample Flask REST API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)