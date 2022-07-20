import hangman_words as words
import hangman_art as art
import random
penalty_limit_point = 7
num_incorrect_word = 0
random_num = random.randint(0,212)
chosen_word = words.word_list[random_num]
chosen_word_list = list(chosen_word)
print(art.logo)
print(chosen_word)
print(chosen_word_list)
guess_letter = ''
#loop letter
while num_incorrect_word < penalty_limit_point and len(chosen_word_list) > 0:
  guess_letter = input("Guess a letter: ")[0].lower()
  num_right_guess = 0
  #loop check all item in list
  for letter in chosen_word_list:
    if letter == guess_letter and len(chosen_word_list) > 0:
      num_right_guess += 1
      if num_right_guess > 0:
        chosen_word_list.remove(guess_letter)
        print(chosen_word_list)
      
  if num_right_guess == 0:
    num_incorrect_word += 1
if len(chosen_word_list) == 0:
  print('You win!')
else:
  print('Game Over! you lose')