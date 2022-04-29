fruits = ["strawberry", "banana", "pear"]
for fruit in fruits:
    print("Would you like a " + fruit + "?")
    print("Would you like a {}".format(fruit))

for number in range(1, 11):
    print("Number {}".format(number))

# Continue statement
for number in range(1, 11):
    if number == 7:
        print("We are skipping number 7.")
        continue
    print("This is the number {}".format(number))


# Pass statement
for number in range(1, 11):
    if number == 3:
        pass
    else:
        print("The number is {}".format(number))



