from flask import Flask, jsonify, request
from flask_cors import CORS
from gamelogic import Game
import uuid
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend
games = {}
@app.route('/api/game', methods=['GET'])
def game():
    global games
    initial_game = Game()
    game_id = str(uuid.uuid4())
    games[game_id] = initial_game

    return jsonify({
        'remaining_tries': initial_game.remaining_tries,
        'letters_used': initial_game.letters_used,
        'game_id': game_id
    })

@app.route('/api/guess', methods=['POST'])
def guess():
    data_dict = request.get_json()
    game_id = data_dict['game_id']
    attempt = data_dict['attempt']
    current_game = games[game_id]
    result, tries = current_game.guess(attempt)
    return jsonify({
        'remaining_tries': tries,
        'game_id': game_id,
        'letters_used': current_game.letters_used,
        'result': result
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)


