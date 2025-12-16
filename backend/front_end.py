import requests

def create_game():
    game_json = requests.get("http://127.0.0.1:5000/api/game")
    return game_json.json()

def guess(game_id, attempt):
    data = {
        "game_id": game_id,
	    "attempt": attempt
    }
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
    result = requests.post("http://127.0.0.1:5000/api/guess", json=data, headers=headers)
    return result.json()

def game_loop(game_id, remaining_tries):
    while remaining_tries > 0:
        attempt = input("type your word: ")
        result = guess(game_id, attempt)
        remaining_tries = result["remaining_tries"]
        letter_used = result["letters_used"]
        letters_result = result["result"]
        print(remaining_tries, letter_used, letters_result)

game = create_game()
game_loop(game["game_id"], game["remaining_tries"])