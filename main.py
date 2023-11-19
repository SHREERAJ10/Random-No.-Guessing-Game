import random

print("Welcome to number guessing game!\n")
l = int(input("Enter lower bound: \n"))
u = int(input("Enter upper bound: \n"))

randomNum = random.randint(l,u)
play = "y"

while play=="y":

    chances = 3
    print(f"You have {chances} chances to guess the number!")

    while chances >0:
        guess = int(input('Enter the number: \n'))
        
        #direct win condition
        if guess == randomNum:
            print(f"{randomNum} is the correct guess. You WIN!")
            break
        
        #TIP: Visualize these conditions in a number line with upper bound, lower bound, randomNumber and guess number to understand the following!

        #way too high condition
        elif guess >= randomNum + 15:
            chances -= 1
            print("You guessed too high!")
            if chances == 0:
                print("YOU LOSE!")
                print(f"The number is {randomNum}")
                break
            print(f"Chances: {chances}")

        #way too low condition
        elif guess <= randomNum - 15:
            chances -= 1
            print("You guessed too low!")
            if chances == 0:
                print("YOU LOSE!")
                print(f"The number is {randomNum}")
                break
            print(f"Chances: {chances}")

        #a little lower guess condition
        elif guess <= randomNum + 15 and guess > randomNum:
            chances-=1
            print("Guess a bit more low")
            if chances == 0:
                print(f"The number is {randomNum}")
                print("YOU LOSE!")
                break
            print(f"Chances: {chances}")

        #a little higher guess condition
        elif guess >= randomNum - 15 and guess < randomNum:
            chances-=1
            print("Guess a bit more high")
            if chances == 0:
                print(f"The number is {randomNum}")
                print("YOU LOSE!")
                break
            print(f"Chances: {chances}")

    play = input("Do you want to play again? y/n\n").lower()
    if play =="y":
        continue
    else:
        print("Thank you for playing!")
        break