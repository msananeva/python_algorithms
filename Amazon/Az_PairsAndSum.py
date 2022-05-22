"""
Create function that takes 2 parameters, an array of integers and an integer.
Print the pair of numbers from the array that add up to the integer.

Questions that can be asked to clarify the problem:
Ask about repeated pairs,
ask about [0,0],
ask about inverted pairs [1,3] and [3,1]

Example: input array [1,3,4,0,9,6] input integer 7. Output [3,4] [1,6]

"""

input = [-1, 9, 3, 5, 2, 6, 1, 4, 0, 5]
s = 8

test = [0, 0]
test2 = []

def pairs(x, sum):
    all_pairs = []
    l = len(x)

    if l == 0 or x == [0, 0]:
        print("add nums")

    for i in range(l):
        for j in range(i + 1, l):
            pair = x[i], x[j]
            if x[i] + x[j] == sum and pair not in all_pairs:
                all_pairs.append(pair)

    if len(all_pairs) == 0:
        print("no pairs of this sum " + format(s) + " in the given arr")
    if len(all_pairs) > 0:
        return all_pairs

print(pairs(input, s))
