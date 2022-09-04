#Tuple: immutable

tuple1=("tomatoe", "onion", "carrot")
print(tuple1[2])
# tuple1[0]="chilli" not possible

for x in tuple1:
    print(x)

print(len(tuple1))

#del tuple1
print(tuple1)

tuple2=(1,2,3,4)
tuple3=tuple1+tuple2
print(tuple3)