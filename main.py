import hangman_words as words
import hangman_art as art
import random
penalty_limit_point = 7
random_num = random.randint(0,212)
chosen_word = words.word_list[random_num]
chosen_word_list = list(chosen_word)
print(art.logo)
print(chosen_word)
print(chosen_word_list)
guess_letter = []
for i in range(0, len(chosen_word_list)):
  input("Guess a letter: ")[0].lower()
print(guess_letter)