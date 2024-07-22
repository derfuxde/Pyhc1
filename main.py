import json
import random


def generate_random_number():
    """Generates a random number and writes it to a JSON file."""
    random_number = random.randint(1, 100)
    with open('random_number.json', 'w') as f:
        json.dump({'number': random_number}, f)

