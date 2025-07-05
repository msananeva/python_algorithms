"""

Write a method which will print out numbers in range
between 1 and a (including it), however:
if number is divisible by 3 print "fizz" instead of number
if number is divisible by 5 print "buzz" instead of number
if number is divisible by both 3 and 5 print "fizzbuzz" instead of number

 """

a = 20

def func():
    for num in range(1, a+1):
        # if number is divisible by both 3 and 5, print "fizzbuzz"
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

func()
