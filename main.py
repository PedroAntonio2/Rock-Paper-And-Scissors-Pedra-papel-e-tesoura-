import random

print("If you want to stop the game, don't enter any available option")

options = ['ROCK','PAPER','SCISSORS']

player_1_wins = 'You Win'
player_2_wins = 'Your Opponent Wins'

wins_player_one = 0
wins_player_two = 0

games = 0

while True:
  first_player_choice = str(input("Make your choice(Rock, Paper, Scissors) ").upper())
  if(first_player_choice != options[0] and first_player_choice != options[1] and first_player_choice != options[2]):
    print("You did not choose any available option")
    break
  second_player_choice = random.choice(options)
  print("----------------------------------------------------------------------")
  print(f"""Round {games+1}:
Your choice: {first_player_choice}
Your opponent's choice: {second_player_choice}""")

  if first_player_choice == second_player_choice:
    print("Draw")
  elif first_player_choice == options[0] and second_player_choice == options[2]:
    wins_player_one += 1
    print(player_1_wins)
  elif first_player_choice == options[1] and second_player_choice == options[0]:
    wins_player_one += 1
    print(player_1_wins)
  elif first_player_choice == options[2] and second_player_choice == options[1]:
    wins_player_one += 1
    print(player_1_wins)
  else:
    wins_player_two += 1
    print(player_2_wins)
  games += 1
  print("----------------------------------------------------------------------")

print(f"""You have won: {wins_player_one} game(s)
Your opponent won: {wins_player_two} game(s)
And you have drawed {games-(wins_player_one + wins_player_two)} game(s)""")
