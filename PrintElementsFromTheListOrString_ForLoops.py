""" Loops """

list = ['CX32', 'GSOF', 'Emily', 'Rex']
for el in list:
    print(el)

for letter in 'Hello':
    print(letter)

""" 
Note: integers are NOT loopable objects.
If you need to loop through the digit and treat them as integers, 
you have to construct this yourself 
"""
"""
We can extract the digits by iterating over the characters in the string version 
of the number and converting each character to an integer
"""

c = 1081287
digits = [int(d) for d in str(c)]


for digit in digits:
    print(digit)
