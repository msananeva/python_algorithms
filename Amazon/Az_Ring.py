"""
Return vowels count from a given string.
input = "This is an awesome string"
vowels = "a e i o y"
output = "a = 2 e = 2 i = 3 o = 1 y = 0"
"""
input = "This is an awesome string"

def vowelsAndNums(input):

    vowels = "a e i o y".split()
    result = {}

    #  initiate an empty dictionary with keys = vowels, values = count = 0
    for letter in vowels:
        result[letter] = 0

    #  iterate over letters in input
    for letter in input:
    #  if the letter is a vowel than add 1 to it's count in the dictionary
        if letter in result:
            result[letter] += 1

    # initiate an empty string
    answer = ""

    # iterate over keys in result and append its values to the answer string
    for key in result:
        count = str(result[key])
        answer += (key + " = " + count + " ")

    return answer

print(vowelsAndNums(input))

