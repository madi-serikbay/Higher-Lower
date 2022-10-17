from art import logo, vs
from game_data import data
from replit import clear
import random

score = 0

def compare(choice, not_choice):
  """This function compares the number of the followers of the chosen celebrity and not chosen celebrity"""
  global score
  if data[choice]['follower_count'] > data[not_choice]['follower_count']:
    score += 1
    return True
  else:
    return False
      
def print_message(a, b):
  """This function prints the introductory information of the celebrity A and the celebrity B"""
  print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}.")
  print(vs)
  print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}.")

def print_result(ans):
  """This function prints out the result and tells if you guessed it right or wrong"""
  if ans == True:
    print(f"You are right! The current score: {score}.")
  elif ans == False:
    print(f"Sorry that's wrong. The final score: {score}.")

def higher_lower():
  clear()
  play = True
  print(logo)
  a = random.randint(0, len(data) - 1)
  b = random.randint(0, len(data) - 1)
  print_message(a, b)
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if choice == 'a':
    play = compare(a, b)
  elif choice == 'b':
    play = compare(b, a)
  else:
    play = False
  if play == True:
    clear()
    while play:
      print(logo)
      print_result(play)
      a = random.randint(0, 49)
      b = random.randint(0, 49)
      print_message(a, b)
      choice = input("Who has more followers? Type 'A' or 'B': ").lower()
      if choice == 'a':
        play = compare(a, b)
      elif choice == 'b':
        play = compare(b, a)
    clear()
    print(logo)
    print_result(play)
  elif play == False:
    clear()
    print(logo)
    print_result(play)

higher_lower()
      
