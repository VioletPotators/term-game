import random


with open(r'C:\Users\Artur Besen\Desktop\term-game\term-game\backend\word-list\words.txt', 'r') as file:
    words2 = file.readlines()
    words = []
    for word in words2:
        words.append(word.strip())



correct_word = random.choice(words)
remaining_tries = 6 
while remaining_tries > 0:
    print("Term game, guess the word")
    print(f"Remaining tries: {remaining_tries}")
    attempt = input("type the word: ")
    if len(attempt) != 5:
        print("Wrong length")
        continue

    if attempt not in words:
        print("invalid word")
        continue

    if attempt == correct_word:
        print("Correct answer")
    else:
        remaining_tries -= 1

