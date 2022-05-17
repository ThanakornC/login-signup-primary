import random
from hangman.words import words

import string

def get_valid_word(words) :
    word = random.choice(words)
    while "-" in word or " " in word:
         word = random.choice(words)

    return word.upper()    

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
           print("you have",lives,"lives left and you have used these letters: ","".join(used_letter))
           word_list = [letter if letter in used_letter else "-" for letter in word]
           print("Current word: "," ".join(word_list))

           user_letter = input ("Guess a letter: ").upper()
           if user_letter in alphabet - used_letter:
               used_letter.add(user_letter)
               if user_letter in word_letters :
                   word_letters.remove(user_letter)
                   print("")
                
                
               else:
                  lives = lives - 1
                  print("\nYour letter,",user_letter,"is not in the word.")
           
           elif user_letter in used_letter:
                print("\nYou have already used that letter.Guess another letter.")

           else:
                print("\nThat is not a valid letter.")

    if lives == 0:
        print("you died,sorry.The word is",word)
    else:
        print("Yes! You won it", word)

if __name__=="__main__":
    hangman()

