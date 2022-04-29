list1 = [1, 2, 4]
list2 = [1, 3, 4]

def mergeTwoLists(list1, list2):
    x = list1 + list2
    return sorted(x)

print(mergeTwoLists(list1, list2))
