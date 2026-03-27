# Program #2: Random Number File Writer
# Josiah Hendley
# 3/26/26
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def main():
    amount = int(input("How many random numbers should the file hold (up to 1000)? "))

    if amount < 1 or amount > 1000:
        print("Please enter a number between 1 and 1000.")
        return

    file = open("random_numbers.txt", "w")

    for i in range(amount):
        number = random.randint(1, 500)
        file.write(str(number) + "\n")

    file.close()
    print("Random numbers written to random_numbers.txt")

main()
