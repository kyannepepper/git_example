import random
print("Hi! I'm going to try to guess your age.")
name = input("What is your name? ")

guessed = False
while(guessed == False):
    guess = random.randint(15,30)
    user_response = input("Are you "+str(guess) + "years old?")
    if user_response == 'y' or user_response == 'Y':
        print(f"haha! {name} is " + str(guess) + " yearse old! I guessed it!")
        guessed = True
    else:
        print("Rats.")