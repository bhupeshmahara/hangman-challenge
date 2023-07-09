#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# list of words to choose from
words = ["badminton", "swimming", "cricket", "football", "basketball", "volleyball"]

# randomly select a word
word = random.choice(words).upper()

# total chances a user have
total_chances = 6
print(f"You have got total {total_chances} chances to guess a word. Good Luck!")

# encrypting the guessed word
guessedWord = "-" * len(word)
print(guessedWord)

while total_chances != 0:
    guessedLetter = input("Guess a letter: ").upper()   # ask the user to guess a letter
    if guessedLetter in word:                           # check if the guessed letter is in the word
        for index in range(len(word)):                  # iterate over each character in the word
            if word[index] == guessedLetter:            # if the guessed letter matches the character
                guessedWord = guessedWord[:index] + guessedLetter + guessedWord[index + 1:] # update the guessedWord at the corresponding index                
        print(guessedWord)
        if guessedWord == word:                         # check if the user has guessed the entire word correctly
            print("Congratulations, you have won the game!")
            break
    else:
        total_chances -= 1                              # decrease the total chances if the guess is incorrect
        print("Incorrect guess, remaining chances are:", total_chances)

# if all chances are exhausted
else:
    print("You lost! Game over. All chances are exhausted!")

print("The actual word was:", word)


# In[ ]:




