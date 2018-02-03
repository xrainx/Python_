import random

def startgame():
    print("Welcome to the Double or quit game!\n75% chance your score is doubled, 25% lose.")
    score = 1
    play = 'y'

    print("Your starting score is: " + str(score) + "\n")

    while score > 0 and play.lower() == 'y':
        play = input("Would you like to double?[y/n]: ")
        if play == 'n':
           print("You end the game and take a score of " + str(score) + " with you!")
           play = input ("would you like to play again?[y/n]")
           print("\n\n")
           startgame()
           continue
        dice = random.randint(0,4)
        if dice != 0: # 75% chance
            score = int(score) * 2
            print("You win! Your score is now: " + str(score) + "\n")

        else:
            score = 0
            play = input("You lost it all!\nPlay again? [y/n]: ")
            if play == 'y':
                score = 1
            else:
                placeholder = input ("Thanks for playing! Press Enter to close")
                quit()

startgame()
