def user_info(name, age = 18, city = "NY"):
    """
    This function print name, age, and city
    from an argument provided to the function.

    ============================
    *args
    allows for unlimited vars to be passed into a function
    without defining them ahead of time

    def add(*args):
        print(sum(args))

    add(2,3,4)
    add(2,4,5,7,10)
    ============================

    *kwargs
    allows for unlimited keyword args to be passed into a function
    without defining them agead of time

    def user(**kwargs):
        print(**kwargs)

    user(name = "Jess", email = "mail@mail.com")
    user(name = "Nate", lastname = "Johnson", age = 40)
    ============================

    Combining arg types
    They must be used in order: formal positional args, *args, *kwargs

    def user(fname, lname, email, *args, **kwargs):
        print("{} {} email is {}".format(fname, lname, email))

    """

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Mila", 34, "Solana Beach")
user_info("Jess")
user_info(age=56, name="Kadeem")


def employee(fname, lname, email, *args, **kwargs):
    print("{} {} email is {}".format(fname, lname, email))


employee("Jess", "Ingrass", "mail@mail.com", 150000, hire_date="Jan 01 2022")



