"""
Write method to find prime numbers between 1 and 100

"""
# 1 is not prime

def primes():
    lower = 1
    upper = 100
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

print(primes())
