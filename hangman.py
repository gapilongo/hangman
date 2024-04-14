import random

print("Welcome to Hangman game!")

words = ["zybra", "classroom", "lovely"]

secret_word = random.choice(words)
print("you got 5 guesses")
shown_words = []

for letter in secret_word:
    shown_words += '_'
print(shown_words)

num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            shown_words[position] = letter
    if guess not in secret_word:
        num+=1
        guesses_left = 5-num
        print(f"you have {guesses_left} left!")
        if num >=5:
            print("You Lose")
            game_over = True
    print(shown_words)

    if "_" not in shown_words:
        print("You Win!")
        game_over = True
