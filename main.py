import json
import random

var r_number = random.randint(1, 100)

def generate_random_number():
    """Generates a random number and writes it to a JSON file."""
    random_number = random.randint(1, 100)
    isnub(random_number, 10)


def isnub(number, isnumber):
    if number > isnumber:
        print("Number is true" , number)
    else:
        print("Number is false" , number, "should be " , isnumber)
    
   
def garv():
   V = random.randint(10,50)
   F = random.randint(V,51)
   print(F , "is on this pos)
   while r_number != F:
      r_number = random.randint(1, 100)
   
   
    