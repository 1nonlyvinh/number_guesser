import random 
name = input("Type your name: ")
print(f"Welcome, {name}")
print("guess a number between 1-15")
number_to_guess = random.randint(1,15)
guess = int(input("Enter your guess: "))

if guess == number_to_guess:
    print("You got it correct! ")
elif guess > number_to_guess:
    print(f"Too high! The number was {number_to_guess}")
else:
    print(f"Too low! The number was {number_to_guess}")


