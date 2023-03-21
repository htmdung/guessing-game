"""A number-guessing game."""

# Put your code here
from random import randint
user_name = input("Hi! What your name? " )
print(f"Nice to meet you, {user_name}")
print(f"{user_name} I'm thinking of a number between 1 and 100. Try to guess my number.")
random_number = randint(1, 100)
guessing_num = ""
guess_limit = 0

while guessing_num != random_number:
    guessing_num = int(input ("Enter your guess number: "))
    guess_limit += 1 
    if guess_limit <= 3:
        if guessing_num > random_number:
            print("Your guess is too high, try again.")
        elif guessing_num < random_number: 
            print("Your guess is too low, try again.")
        else:
            print(f"Well done, {user_name}!. You found my number in {guess_limit} tries!")
    else:
        print(f"Sorry, you are out of guessing limit number")
        break


