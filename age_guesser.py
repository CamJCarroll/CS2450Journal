import random

guess_age = True
guess = random.randrange(15,31)

print("Greetings! I am going to guess your age.")
name = input("What is your name? ")
print(f"Hi {name}, I will guess an age and you will tell me yes or no.")
print("Please enter y for yes and n for no.")
while guess_age == True:
    response = input(f"Is your age {guess}? ")
    if response == "n":
        print("Rats.")
        guess = random.randrange(15,31)
    elif response == "y":
        print(f"{name} is {guess} years old.")
        guess_age = False
    else:
        print("Invalid response, please enter y or n.")