input = [8, 3, 0, 0, 22, 22, 4]
input_to_set = set(input)

set_to_list = list(input_to_set)

set_to_list.sort()

answer = set_to_list[1]

print(answer)
