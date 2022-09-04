#Set:unordered and unindexed

set1={"cat","dog","rat"}
print(set1)
#print(set1[0]) not allowed

for x in set1:
    print(x)

print("cat" in set1)

set1.add("onion")
print(set1)

set2={1,2,3,4}
set3=set1.union(set2)
print(set3)