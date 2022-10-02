import random
import data
import choices

#class_data = data.create_data()
class_data = choices.choices
#format: dict {CourseNumber: "Name"}
keys = list(class_data.keys())


def play_game():
  score = 0
  while True:
    option1 = random.choice(keys)
    option2 = random.choice(keys)
    while option2 == option1:
      option2 = random.choice(keys)
    print("Which course has a higher number? " + class_data[option1] +
          " (1) or " + class_data[option2] + " (2)")
    choice = int(input("Type in 1 or 2: "))
    while choice not in [1, 2]:
      choice = int(input("Invalid input, please type in 1 or 2: "))
    if (choice == 1 and option1 > option2) or (choice == 2
                                               and option2 > option1):
      print("Correct! Option 1 is " + str(option1) + ". Option 2 is " +
            str(option2) + ".")
      print("-----------------------")
      score += 1
    else:
      print("Wrong! Option 1 is " + str(option1) + ". Option 2 is " +
            str(option2) + ".")
      print("-----------------------")
      break

  print("Your final score was", score)
  print("Play again?")
  answer = input("Type in \"Yes\" if you want to play again.")
  if answer == "Yes":
    play_game()


play_game()
