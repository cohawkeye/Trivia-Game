'''
Title: Trivia Game
Author: Grace
Description: A Trivia Game
'''
def main():
    dict = {}
    done = False
    while not done:
        print("==========")
        print("S - Start")
        print("D - Display")
        print("Q - Quit")
        choice = input("Choice: ")
        if choice == "S":
            print("Starting Game")
            name = input("What's your name? ")
            print("Welcome to the game", name + "!")
            print("Categories")
            print("-Sports")
            print("-History")
            print("-Pop Culture")
            print("-Animals")
            answerA = "sports"
            answerB = "history"
            answerC = "pop culture"
            answerD = "animals"
            dict[name] = score = 0
            guess = input("What category are you interested in? \n")
            cleanedGuess = guess.lower().strip()
            if cleanedGuess == answerA:
                answerAA = "olympia"
                guessAA = input("Where was the first Olympics? \n")
                cleanedGuessAA = guessAA.lower().strip()
                if cleanedGuessAA == answerAA:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerAB = "23"
                guessAB = input("How many Grand Slams has Serena Williams won? \n")
                cleanedGuessAB = guessAB.lower().strip()
                if cleanedGuessAB == answerAB:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerAC = "golf"
                guessAC = input("What is the only sport to be played on the moon? \n")
                cleanedGuessAC = guessAC.lower().strip()
                if cleanedGuessAC == answerAC:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
            if cleanedGuess == answerB:
                answerBA = "1776"
                guessBA = input("What year did America gain independence?\n")
                cleanedGuessBA = guessBA.lower().strip()
                if cleanedGuessBA == answerBA:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerBB = "theodore roosevelt"
                guessBB = input("who was the first American to win a Nobel Peace Prize?\n")
                cleanedGuessBB = guessBB.lower().strip()
                if cleanedGuessBB == answerBB:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerBC = "germany"
                guessBC = input("Where did Albert Einstein live before moving to the United States?\n")
                cleanedGuessBC = guessBC.lower().strip()
                if cleanedGuessBC == answerBC:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
            if cleanedGuess == answerC:
                answerCA = "12"
                guessCA = input("How many Grammys has Taylor Swift won?\n")
                cleanedGuessCA = guessCA.lower().strip()
                if cleanedGuessCA == answerCA:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerCB = "10"
                guessCB = input("How many original albums has Taylor Swift released?\n")
                cleanedGuessCB = guessCB.lower().strip()
                if cleanedGuessCB == answerCB:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerCC = "taylor swift"
                guessCC = input("Who has the most American Music Awards wins?\n")
                cleanedGuessCC = guessCC.lower().strip()
                if cleanedGuessCC == answerCC:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
            if cleanedGuess == answerD:
                answerDA = "a clowder"
                guessDA = input("What is a group of cats called?\n")
                cleanedGuessDA = guessDA.lower().strip()
                if cleanedGuessDA == answerDA:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerDB = "nose"
                guessDB = input("The age of a sea lion is determined by its...?\n")
                cleanedGuessDB = guessDB.lower().strip()
                if cleanedGuessDB == answerDB:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
                answerDC = "seahorse"
                guessDC = input("What male sea creature gives birth to its young?\n")
                cleanedGuessDC = guessDC.lower().strip()
                if cleanedGuessDC == answerDC:
                    print("Correct!")
                    dict[name] = score = score+1
                else:
                    print("Nope!")
            for k, v in dict.items():
                print("Congratulations " + str(k) + " you got " + str(v) + " right!")
        elif choice == "D":
            print("Leaderboard")
            print(dict)
        elif choice == "Q":
            print("Exiting Program")
            done = True

main()
