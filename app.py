from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my API",
        "status": "active",
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/info')
def info():
    return jsonify({
        "student_name": "YOUR_NAME",
        "course": "YOUR_COURSE",
        "api_version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)