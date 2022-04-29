input = "Aaaaabbbc".lower()

append_times = input.count("a")

def moveToEnd(x):
    b = x.replace('a', "")
    for i in range(append_times):
        b += 'a'
    return(b)

print(moveToEnd(input))
