import random


def game():
  game_over = False
  lives = 0
  random_num = random.randrange(1, 101)
  print("Let's play a guessing game!")
  difficulty = input("Choose difficulty: Easy or Hard? \n")
  if difficulty.lower() == "easy":
    lives = 10
  else:
    lives = 5
  while game_over == False:
    guess = input("Guess a number between 1 and 100! \n")
    guess = int(guess)
    if guess > random_num:
      print("Too High!")
      lives -= 1
      print (f"You have {lives} tries reamianing.")
    if guess < random_num:
      print("Too Low!")
      lives -= 1
      print (f"You have {lives} tries reamianing.")
    if guess == random_num:
      print("You got it! You Win!")
      game_over = True
    if lives == 0:
      print(f"You Lose! The number was {random_num}")
      game_over = True      
  play_again = input("Do you want to play again? y/n \n")
  if play_again.lower() == "y":
    game()

game()