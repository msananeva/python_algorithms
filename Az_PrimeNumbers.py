"""
Prime Numbers.
Return 'True' if 'n' is a prime number. False otherwise
"""


def is_prime(n):
    if n == 1:
        return False  # 1 is not prime

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


# Test
for n in range(1, 21):
    print(n, is_prime(n))
