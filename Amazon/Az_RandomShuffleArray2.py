""" You have an array of characters.
How would you randomly sort its elements?
The random number generator is already implemented.
"""

from random import randint

arr = ["This", "is", "a", "string"]
l = len(arr)

def randomize(arr, l):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(l - 1, 0, -1):
        # Pick a random index from 0 to i
        j = randint(0, i + 1)

        # Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
    return arr

print(randomize(arr, l))