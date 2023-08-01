 #Number Guessing Game Objectives:
from art import logo
import random 
import clear
# Include an ASCII art logo.
def makeAGuess():
  print(logo)
  print("\nWelcome to the Number Guessing Game !")
  print("I am Thinking of a Number Between 1 to 100 .")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  # Allow the player to submit a guess for a number between 1 and 100.
  number = random.randint(1, 100)
  print("shhh "+str(number))
  def turns():
    current_turn = 0
    for turn in range(numberOfTurns):
      current_turn += 1
      guess = int(input("Make a Guess: "))
      print(guess)
      if guess > number:
        print("Too High")
      elif guess < number:
        print("Too low")
      elif guess == number:
        print("You Guessed Correct !!")
        break
      turnsLeft = numberOfTurns - current_turn
      print("You Have "+str(turnsLeft)+" Turns Left")
      
  if difficulty == "easy":
    numberOfTurns = 10
    turns()
  elif difficulty == "hard":
    numberOfTurns = 5
    turns()
makeAGuess()

restart = input("Do you want to play again ? type 'yes' or 'no': ")
if restart == "yes":
  clear.clear()
  makeAGuess()
elif restart  ==  "no":
  clear.clear()
  print(logo)
  print("\n Thank you For Playing <3 .")
          


  

