"""
Naming a Variable
1. Start with a letter or underscore(_)
2. Cannot start with number
3. Use alphanumeric (A-Z, a-z, 0-9, _)
4. Case sensitive
"""
a=10
name="Praveen"
num=5.32
x=10j
python=True
java=False
print(a)
print(name)
print(num)
print(x)
print(python)
print(java)

print(type(a))
print(type(name))
print(type(num))
print(type(x))
print(type(python))
print(type(java))


a=10
b=10
c=10
print(a)
print(b)
print(c)

a=b=c=10
print(a)
print(b)
print(c)

a, b, c = 10, 20, 30
print(str(a)+" "+str(b)+" "+str(c))
