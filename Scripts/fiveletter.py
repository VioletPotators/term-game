with open('palavras.txt', 'r') as file:
    words = file.readlines()

words_fixed = []
for word in words:
    if len(word) == 6:
        words_fixed.append(word)
with open('words.txt', 'w') as file:
    words_fixed = "".join(words_fixed)
    file.write(words_fixed)