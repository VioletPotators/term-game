import random

        
with open(r'C:\Users\Artur Besen\Desktop\term-game\term-game\backend\word-list\words.txt', 'r') as file:
    words2 = file.readlines()
    words = []
    for word in words2:
        words.append(word.strip().lower())


class Game:
    correct_word = ""
    remaining_tries = 0
    letters_used = []

    def __init__(self) -> None:
        self.correct_word = self.choose_word()
        self.remaining_tries = 5

    
    def choose_word(self):
        correct_word = random.choice(words)
        return correct_word

    def guess(self, attempt):
        if len(attempt) != 5:
            return "Wrong length", self.remaining_tries
        if attempt not in words:
            return "invalid word", self.remaining_tries

        if attempt == self.correct_word:
            return "Correct answer", self.remaining_tries

        else:
            attempt_letters = list[str](attempt)
            correct_word_letters = list(self.correct_word)


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
                
            final_list = []
            for letter_index, color in final_check.items():
                letter = letter_index[0]
                if color == "yellow":
                    final_list.append(f"\033[0;36m{letter}\033[0m")
                    if f"\033[0;36m{letter}\033[0m" not in self.letters_used:
                        self.letters_used.append(f"\033[0;36m{letter}\033[0m") 
                elif color == "green":
                    final_list.append(f"\033[0;32m{letter}\033[0m")
                    if f"\033[0;32m{letter}\033[0m" not in self.letters_used:
                        self.letters_used.append(f"\033[0;32m{letter}\033[0m")
                else:
                    final_list.append(letter)
                    if letter not in self.letters_used:
                        self.letters_used.append(letter)


            self.remaining_tries -= 1
            return "".join(final_list), self.remaining_tries
            

    def game_loop(self):   
        while self.remaining_tries > 0:
            attempt = input("type your word: ")
            result = self.guess(attempt)
            print(result)

# Game1 = Game()
# Game1.game_loop()