str = "AaaAAAaaaBbbbcbccccc".lower()

def mostOccurringChar(x):
    all_freq = {}
    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return max(all_freq, key=all_freq.get)

print("Most occurring char is: ", mostOccurringChar(str))

count = str.count("a")

def moveAToTheEnd(x):
    b = x.replace("a", "")
    for i in range(count):
        b += "a"
    return(b)

print("New string: ", moveAToTheEnd(str))
