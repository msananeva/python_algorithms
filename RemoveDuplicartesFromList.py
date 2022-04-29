""" Remove Duplicates From The List """

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

#______________________________________________

el = ["a", "b", "a", "c", "c"]

def listWithNoDups(x):
  return list(dict.fromkeys(x))

nodups = listWithNoDups(el)

print(nodups)
