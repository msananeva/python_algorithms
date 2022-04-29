""" Random """

# Display 10 random numbers from interval [0, 1)

import random

for i in range(10):
    print(random.random())

#________________________________________

# Display 10 random numbers from interval [3,7)

import random

for i in range(10):
    print(random.uniform(3, 7))

#_________________________________________

# random INTEGER from interval [3,6]

import random

for i in range(10):
    print(random.randint(3, 6))
#_________________________________________

# rock, paper, scissors

import random

outcomes = ["rock", "paper", "scissors"]

for n in range(10):
    print(random.choice(outcomes))
