"""  There are N strings.
Returned strings: words should be in the same order AND
letters in words should be rotated
"""

a = int(input("Enter a number: "))
strings = []

for i in range(a):
    strings.append(input("sample string {}: ".format(i+1)))

for s in strings:
    rotated = s[::-1]  # Changes the order of letters
    words = rotated.split()  #  bc we need words to be split by space, not by letter
    reversedStrings = " ".join(reversed(words))  # Changes the order of words ONLY
    print(reversedStrings)

#______________________________________

""" Fibonacci. Input is 5 8 4 . Give the 4th number in a fibonacci sequence 
(the sequence starts with 5 in this example. The sequence is [5,8,13,21....])  """

input = input().split()  # we use split instead of list bc the input can include the number with 2 chars

a1 = int(input[0])
a2 = int(input[1])
x = int(input[2])

def fibonacci(n):
    if n == 1:  #  first number in a given fibonacci sequence
        return a1
    elif n == 2:
        return a2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


el = fibonacci(x)
print(el)

#________________________________________

""" 
Rearrange chars in a string in a desc order.  Ex. Sandy -> ySnda
"""

b = list(input())

b.sort(key = lambda x: x.lower())  #  sort case-insensitive
b.reverse()  #  reverse to display in desc order
joined = "".join(b)  #  convert a list into a string

print(joined)

#_________________________________________

""" 
Given a string "XX--" or "0....."
Output the percentage of the task which is already completed, as an integer.

The key here is there are 2 types of chars: which ones are on the left, 
which ones are on the right
"""

progressBar = list("XX--")

firstCharacter = progressBar[0]

remainingCharacters = progressBar[1:]  #slicing the list

countCompleted = 1

for char in remainingCharacters:
    if char == firstCharacter:
        countCompleted += 1
    else:
        break

percentage = int((countCompleted / len(progressBar)) * 100)

print(percentage)
