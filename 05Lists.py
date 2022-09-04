# Collections
# List, Tuple, set, Dictionary

# LIST
list1 = ["onion", "tomoto", "carrot"]

print(list1)
print(len(list1))
print(list1[2])
list1[0]="cabbage"
print(list1)
for x in list1:
    print(x)

list1.append("mangoe")
list1.insert(0,"grape")
print(list1)
list1.remove("mangoe")
print(list1)
list1.clear()
del list1
print(list1)

list2 = [10, 20, 30, 40]
sum = list2[0] + list2[2]
print(sum)
