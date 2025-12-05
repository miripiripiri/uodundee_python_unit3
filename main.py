from random import randint

# Generates main menu for player with option to play the game or view scores

def menu():
    print("Welcome to Higher or Lower!")
    print("Option 1: Play!")
    print("Option 2: View Previous Scores")
    print("Option 3: View highest score")


# Takes the players choice of play or view scores and checks player has used a valid input

    menuOption = input("Pick an option\n")

    if menuOption == "1":
        playGame()

    elif menuOption == "2":

        try:
            with open("scores.txt", "r") as file:
                 print(file.read())
        except:
            print("Error")

        finally:
            menu()

    elif menuOption == "3":

        try:
            with open("scores.txt", "r") as file:

                 highestScorePlayer = ""
                 highScore = 0

                 for line in file:
                     try:
                         nextScore = int(line[-2:])

                         if nextScore > highScore:
                             highScore = nextScore
                             highestScorePlayer = line

                         elif nextScore == highScore:
                             highestScorePlayer = highestScorePlayer + "\nand\n" + line

                     except:
                         nextScore = int[-1:]

                         if nextScore > highScore:
                            highScore = nextScore
                            highestScorePlayer = line

                         elif nextScore == highScore:
                            highestScorePlayer = highestScorePlayer + "\nand\n" + line

        except:

            print("Error")

        finally:

            print(highestScorePlayer)
            menu()

    else:
        print("Whoops! Please type 1 or 2")
        menu()



def playGame():
    username = input("Choose your username: ")

# Setting the difficulty for the game

    print("Pick a difficulty setting.")
    print("1 = Easy")
    print("2 = Medium")
    print("3 = Hard")

    difficulty = input("\n")
    x = 1000

    if difficulty == "1":
        pass

    elif difficulty == "2":
        x = 100

    elif difficulty == "3":
        x = 10

    else:
        print("Invalid input. Try again.")
        playGame()

    score = 0
    setNum = randint(0, x)
    hasLost = False


# Runs the game and saves the scores to a text file

    while hasLost == False:

        print(setNum)
        print("Higher or lower?")
        guess = input("Type > or <\n")
        newNum = randint(0, x)

        if (guess == ">" and newNum > setNum) or (guess == "<" and newNum < setNum):
            setNum = newNum
            print("Well done!")
            score += 1

        elif (guess == ">" and newNum < setNum) or (guess == "<" and newNum > setNum):
            print("You lose :(")
            hasLost = True
            print("Your score is " + str(score))

            try:
                with open("scores.txt", "a") as file:
                    file.write(username + ": " + str(score) + "\n")

            except:
                print("Error saving score")

            finally:
                menu()


        elif guess != "<" or ">":
            print("Invalid input. Try again.")

menu()
