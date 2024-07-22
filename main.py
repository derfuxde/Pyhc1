import json
import random


def generate_random_number():
    """Generates a random number and writes it to a JSON file."""
    random_number = random.randint(1, 100)
    isnub(random_number, 10)


def isnub(number, isnumber):
    if number > isnumber:
        print("Number is true" , number)