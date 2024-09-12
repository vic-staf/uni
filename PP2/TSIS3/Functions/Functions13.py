import random
def Guess_Number(start, end):
    guess = random.randint(start, end)
    while True:
        tries = 1
        name = input("Hello! What is your name?")
        print("Well, " + name + ", I am thinking of a number between 1 and 20.")
        attempt = int(input("Take a guess."))
        while attempt != guess:
            tries += 1
            if attempt < guess:
                print("Your guess is too low")
                attempt = int(input("Take a guess."))
            else:
                print("Your guess is too high")
                attempt = int(input("Take a guess."))
        print(f"Good job, {name}! You guessed my number in {tries} guesses!")
        break


# Guess_Number(1, 20)