from random import choice

def ask_move():
  while True:
    player_move = input("Type your move (rock, paper, scissors): ").lower()
    if player_move in ['rock', 'paper', 'scissors']:
      return {"player": player_move, "computer": choice(["rock", "paper", "scissors"])}
    else:
      print("invalid option.")

def compute_winner(move):
  move_value = {"rock":1, "paper":2, "scissors":3}
  print("The computer played: ", move["computer"])
  if move["player"] == move["computer"]:
    print("It's a tie!")
  elif (move_value[move["player"]])%3 == (move_value[move["computer"]]+1)%3:
    print("You won! :D")
  else:
    print("You lost :(")

compute_winner(ask_move())