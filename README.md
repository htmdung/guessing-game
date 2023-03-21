# guessing-game
The game will work like this:

The computer will choose a random number between 1–100 and ask the user to guess the number

Once the user guesses, the computer will tell the user if their guess was too high or too low

The game is over once the user guesses the computer’s number. When the game is over, the computer the total number of guesses the user made before getting the right answer.

Here’s a rough pseudocode outline of the program that gave this output:

greet player

get player name

choose random number between 1 and 100

repeat forever:

    get guess

    if guess is incorrect:

        give hint

        increase number of guesses

    else:
    
        congratulate player