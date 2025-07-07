"""
Prime Numbers.
Return 'True' if 'n' is a prime number. False otherwise
"""


def is_prime(num):
    if num < 2:
        return False  # 1 is not prime

    for d in range(2, num):
        if num % d == 0:
            return False
    return True


# Test
for num in range(1, 21):
    print(num, is_prime(num))
