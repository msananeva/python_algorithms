"""The list of all users"""


class User:

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln


print(User.__doc__)  # to see what this class is for

user1 = User("Mila", "Tarasov")
user1.address = "Solana Beach"  # We can add an additional attribute

print(user1.__dict__)
