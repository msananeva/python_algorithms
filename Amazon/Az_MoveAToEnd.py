""" Move all "a" to the end """

input = "AaaaaAbbbc"

def move_all(x):
    all_a = ""
    the_rest = ""
    for char in x:
        if char.lower() == "a":
            all_a += char
        else:
            the_rest += char
    return the_rest + all_a

print(move_all(input))
