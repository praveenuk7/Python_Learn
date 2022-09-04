# Dictionary

dict1 = {
    "name" : "John",
    "email" : "john@gmail.com",
    "phone" : 123456789
}
print(dict1)
a=dict1["name"]
a=dict1.get("phone")
print(a)

dict1["name"]="smith"
print(dict1)

for x in dict1:
    print(x)
for x in dict1:
    print(dict1[x])
for x,y in dict1.items():
    print(x,y)

print(len(dict1))

dict1["age"]=25

print(dict1)

dict1.pop("email")
print(dict1)

del dict1["age"]
print(dict1)