""" Merge two lists without duplicates """

list1 = [1, 2, 4, 7]
list2 = [1, 3, 4]

def mergeTwoLists(list1, list2):
    no_dups = []
    joined = list1 + list2
    sorted_list = sorted(joined)
    for num in sorted_list:
        if num not in no_dups:
            no_dups.append(num)
    return no_dups



print(mergeTwoLists(list1, list2))
