from flask import Flask
from flask import jsonify, make_response

app = Flask('__main__')

@app.route('/')
def home():
    return make_response(jsonify({
        "data": 'welcome',
        "status": 200
    }), 200)

if __name__ == '__main__': app.run()
