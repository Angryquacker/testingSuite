from test import returnCheck
import random

def idk():
    return random.randint(0, 10)

for i in range(10):
    returnCheck(idk, random.randint(0, 10))
    
input("")
