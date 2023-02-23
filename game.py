"""A number-guessing game."""

# Put your code here
import random
user_name = input("Hi! What your name? " )
print(f"Nice to meet you, {user_name}")
print (f"{user_name} I'm thinking of a number between 1 and 100. Try to guess my number.")
random_number = random.randint(1, 100)
print(f"{random_number}")
count = 0
while True:
    guessing_num = int(input ("Enter your guess number: "))
    count += 1 
    if guessing_num != random_number:
        if guessing_num > random_number:
            print("Your guess is too high, try again.")
        else: 
            print("Your guess is too low, try again.")
    else:
        print(f"Well done, {user_name}!. You found my number in {count} tries!")
        break;
