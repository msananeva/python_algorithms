"""
Write method to find prime numbers between 1 and 100

"""
# 1 is not prime

def primes():
    lower = 2
    upper = 100
    result = []
    for num in range(lower, upper + 1):
        for d in range(2, num):
            if num % d == 0:
                break
        else:
            result.append(num)
    return result

print(primes())
