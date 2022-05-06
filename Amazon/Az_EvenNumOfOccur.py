"""
Given a list of items, every element appears an odd # of times.
One element appears an even number of time.
Return the element that appears an even # of times
"""

input = ["sun", "sandy", "ocean", "sandy"]

def evenOccurInList(x):
    for el in x:
        occur = x.count(el)
        if occur % 2 == 0:
            return el

print(evenOccurInList(input))
