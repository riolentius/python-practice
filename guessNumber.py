import random
attempt_list = []
def show_score():
    if len(attempt_list) <= 0:
      print("there is no high score, you are the first")
    else :
      print("the current high score is {} attempt".format(min(attempt_list)))

  
def start_game():
  random_number = int(random.randint(1,10))
  print("Hello Traveler")
  player_name = input("Name: ")
  wanna_play = input("Hi, {} would you like to play? (Yes / No)".format(player_name))
  attempts = 0
  show_score()
  while wanna_play.lower() == "yes":
    try:
      guess = input("Pick number 1 to 10 ")
      if int(guess) < 1 or int(guess) >10 :
        raise ValueError("Please Guess between 1 to 10")
      if int(guess) == random_number:
        print("Nice")
        attempts += 1
        attempt_list.append(attempts)
        print("It took {} attemps".format(attempts))
        play_again = input("Play Again? (Yes / No) ")
        attempts = 0
        show_score()
        random_number = int(random.randint(1,10))
        if play_again.lower() == "no":
          print("That's Cool, have a good one!")
          break
      elif int(guess) > random_number:
        print("Its Lower")
        attempts += 1
      elif int(guess) < random_number:
        print("Its Higher")
        attempts += 1
    except ValueError as err:
      print("Oh no, it is not valid, try again...")
      print("({})".format(err))
  else:
    print("Thats Cool, Have a good one")
if __name__ == '__main__':
  start_game()