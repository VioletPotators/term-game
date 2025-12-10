import random


with open(r'C:\Users\Artur Besen\Desktop\term-game\term-game\backend\word-list\words.txt', 'r') as file:
    words2 = file.readlines()
    words = []
    for word in words2:
        words.append(word.strip().lower())



correct_word = "oucas"#random.choice(words)
remaining_tries = 6     
print("Term game, guess the word")
while remaining_tries > 0:

    print(f"Remaining tries: {remaining_tries}")
    attempt = input("type the word: ")
    if len(attempt) != 5:
        print("Wrong length")
        continue

    if attempt not in words:
        print("invalid word")
        continue

    if attempt == correct_word:
        print(f"Correct answer")
        break
    else:
        attempt_letters = list[str](attempt)
        correct_word_letters = list(correct_word)


        amount_correct = {}
        for letter in correct_word_letters:
            if letter not in amount_correct:
                amount_correct[letter] = 0
            amount_correct[letter] += 1

        final_check = {}
        for i, letter in enumerate[str](attempt_letters):
            if letter == correct_word_letters[i]:
                final_check[letter + str(i)] = "green"
                amount_correct[letter] -= 1

                if amount_correct[letter] < 0:
                    for letter_index, color in final_check.items():
                        letter_inside = letter_index[0]
                        index = letter_index[1]
                        if letter == letter_inside and color == "yellow":
                            final_check[letter_index] = "none"
                            amount_correct[letter] += 1

                continue
            if letter in correct_word_letters and amount_correct[letter] > 0:
                final_check[letter + str(i)] = "yellow"

                amount_correct[letter] -= 1
                continue
            final_check[letter + str(i)] = "none"


        print("".join(final_check))
        remaining_tries -= 1
        

print(f"The word was: {correct_word}")

 