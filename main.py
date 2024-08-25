
import random
from art import logo

def guess_number(attempts, secret_number):
  """Guessing a number for a number of attempts, based both on user input"""
  print(f"You have {attempts} attempts remaining to guess the number.")
  
  while attempts > 0:
    current_attempt = input("Make a guess: ")
    if not current_attempt.isnumeric():
      print("Wrong input, insert a number.")
    else:
      current_attempt = int(current_attempt)
      if current_attempt > secret_number:
        print("Too high.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number. ") 
      elif current_attempt < secret_number:
        print("Too low.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number. ")
      elif current_attempt == secret_number:
        print(f"You got it! The answer was {secret_number}.\nGoodbye :-)")
        return

  print("You've run out of guesses, you lose.")

def guessing_game():
  """Main function that initiates the guessing game"""
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

  secret_number = random.randint(0, 100)
  easy = 10 
  hard = 5
  
  print(f"Pssst, the correct answer is {secret_number}")
  correct_diff_input = False

  while not correct_diff_input:
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_choice == 'easy':
      guess_number(easy, secret_number)
      correct_diff_input = True
    elif difficulty_choice == 'hard':
      guess_number(hard, secret_number)
      correct_diff_input = True
    else:
      print("Wrong input, type 'easy' or 'hard'.")
      
guessing_game()






  
