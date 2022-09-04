text = "Learn Python"
subText="""
This is a complete tutorial 
for aspiring beginners
"""
print(text)
print(subText)

print(text[0])
print(text[1:])
print(text[0:3])
print(len(text))
print(len(subText))
print(text.lower())
print(text.upper())
print(text.replace("P","j"))

a="Learn "
b="Python "
c="with me"
c=a+b+c
print(c)

# placeholders
name = "Praveen"
age = 25
text = "My name is {}, Iam {} years old"
print(text.format(name, age))