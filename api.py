from flask import Flask, jsonify
from datetime import datetime
from flask import request
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "API is working!",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        "message": "This is a test endpoint",
        "status": "success"
    })

# For local testing
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)