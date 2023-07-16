# Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(f"the chosen word is {chosen_word}")

list_of_chosen_word = []
len_of_chosen_word = len(chosen_word)
chances = len_of_chosen_word

for n in range(len_of_chosen_word):
    list_of_chosen_word.append("_")
print(list_of_chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while chances > 0:
    guess = input("Guess a letter from the word: ").lower()

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if "_" in list_of_chosen_word:
        for position in range(len_of_chosen_word):
            letter = chosen_word[position]
            if letter == guess:
                list_of_chosen_word[position] = letter
        print(list_of_chosen_word)

        if guess not in chosen_word:
            chances -= 1
    else:
        print("YOU WON!!!!!")
print("YOU ran out of chances....")