import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock,paper,scissors]
user_choice = int(input("Enter 0 for Rock, 1 for Paper, and 2 for Scissors"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid Number")
else:
    print(images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(images[computer_choice])
    print(computer_choice)
    if computer_choice == user_choice:
        print("Draw! !")
    elif computer_choice == 0 and user_choice == 2:
        print ("You Lose")
    elif computer_choice > user_choice:
        print("You Lose")
    else:
        print("You Win! !")