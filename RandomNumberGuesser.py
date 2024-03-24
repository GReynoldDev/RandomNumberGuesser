import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess (1,100): "))
            
    if guess == secret_number:
        print("Congratulations! you guessed the number.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")