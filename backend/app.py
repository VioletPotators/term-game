from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Flask API is running'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'message': 'Hello from Flask API!',
        'data': [1, 2, 3, 4, 5]
    })

@app.route('/api/about', methods=['GET'])
def about():
    return jsonify({
        'title': 'About',
        'description': 'This is a full-stack application with Flask and React'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

