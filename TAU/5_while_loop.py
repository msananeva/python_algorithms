# temp = 37
# while temp > 32:
#     print("Water, bc the temperature is {}".format(temp))
#     temp -= 1
# print("Ice")

"""
Loop controls

Break
end the loop. Go to the next statement in the program(outside the loop)

Continue
skip current part of the loop. Move to the next part of the loop

Pass
skip any part of the loop where "pass" appears

"""

temp_f = 35
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break
