# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over!")
#         break
# else:
#     print("Aren't you glad you got out of there!")

import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0       # initialize to any number outside if the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game Over!")
        break
    if guess == answer:
        print("Well done, you guessed it!")
        break
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
