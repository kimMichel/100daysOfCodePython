import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

choosed_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choosed_option == 0:
    print(rock)
elif choosed_option == 1:
    print(paper)
else:
    print(scissors)

print("Computer choose:\n")

computer_choose = random.randint(0, 2)

if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
else:
    print(scissors)

win_message = "You win!"
lose_message = "You lose."

if choosed_option == computer_choose:
    print("Draw")
elif choosed_option == 0 and computer_choose == 1:
    print(lose_message)
elif choosed_option == 0 and computer_choose == 2:
    print(win_message)
elif choosed_option == 1 and computer_choose == 0:
    print(win_message)
elif choosed_option == 1 and computer_choose == 2:
    print(lose_message)
elif choosed_option == 2 and computer_choose == 0:
    print(lose_message)
elif choosed_option == 2 and computer_choose == 1:
    print(win_message)