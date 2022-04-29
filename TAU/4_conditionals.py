def fee():
    """ Defines if user should or should NOT pay for the luggage"""


lug_weight = int(input("Please enter your luggage weight: "))
if lug_weight < 20:
    print("No fee")
elif lug_weight in range(20, 30): #20-29 lbs
    print("The fee is 10 USD")
else:
    print("The max fee is 25 USD")

# =====================================================

name = input("What's your username?")
if name == "Mila":
    print("Hello, nice to see you {}!".format(name))
print("Have an amazing day {}!".format(name))

# =====================================================

