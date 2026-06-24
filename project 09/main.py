'''
1 = snake
2 = water
3 = gun
'''

import random

choices = {
    1: "Snake",
    2: "Water",
    3: "Gun"
}

user = int(input("Enter 1 for Snake, 2 for Water, 3 for Gun: "))

robot = random.randint(1, 3)

if user == robot:
    print(f"Both chose {choices[user]}. It's a tie!")
elif (user == 1 and robot == 2) or (user == 2 and robot == 3) or (user == 3 and robot == 1):
    print(f"You chose {choices[user]} and the robot chose {choices[robot]}. You win!")
else:
    print(f"You chose {choices[user]} and the robot chose {choices[robot]}. You lose!")