import random
print("Hi! I'm going to try to guess your age.")
name = input("What is your name? ")

guessed = False
numberOfGuesses = 0
while(guessed == False):

    guess = random.randint(10,30)
    user_response = input("Are you "+str(guess) + "years old?")
    numberOfGuesses += 1
    print(numberOfGuesses)
    if numberOfGuesses == 5:
        print("Man this game was too tough. I give up.")
        age = input("How old are you?")
        print("I loose and you win " + str(age) + " years of free membership at contact")
        guessed = True
    elif user_response == 'y' or user_response == 'Y':
        print(f"haha! {name} is " + str(guess) + " yearse old! I guessed it!")
        guessed = True
    else:
        print("Rats.")