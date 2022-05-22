""" You have an array of characters.
How would you randomly sort its elements?
The random number generator is already implemented.
"""

from random import randint

arr = ["This", "is", "a", "string"]
l = len(arr)

def randomize(arr, l):
    # Start from the last element and swap one by one. We don't need to run for the first element that's why i > 0
    for i in range(l - 1, 0, -1):
        j = randint(0, l-1)  # Pick a random index from 0 to l-1

        arr[i], arr[j] = arr[j], arr[i]  # Swap arr[i] with the element at random index
    return arr

print(randomize(arr, l))