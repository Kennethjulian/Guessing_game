#:1 import random module
import random
#:2 have user intr a random number

top_range = input("Type a number: ")
# check to see if user entered a number
#if user intered a number convert it to a interger
if top_range.isdigit():
    top_range = int(top_range)
# if user enters a number less than 0 quit game
    if top_range <= 0:
        print("Bruhh type a number larger than 0 next time")
        quit()
else:  #if user enters anything other than a digit quit game
    print("Sooo thats a number to you??")
    quit()

random_num = random.randint(0,top_range)
# Keep track of users guesses
guesses = 0
#keep asking user to guess a number untill they get it correct
while True:
    guesses += 1 # every time the user guesses this will add one
    user_guess = input("Make a guess chosen one!")
    if user_guess.isdigit(): # check if the user entered a number
        user_guess = int(user_guess) # convert string into an interger
    else: # if user does not enter a number continue the loop
        print("Sooo thats a number to you??")
        continue
# if user guess is correct brake the while loop
    if user_guess == random_num:
        print("Wow you got it what an exciting life you lead!")
        break
    else: # I could have used elif
        if user_guess > random_num:
            print("Nope Too High!")
        else:
            print("Nope To Low!")
#print how many guesses it took the user
print("you got it in", guesses, "guesses")