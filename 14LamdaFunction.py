#Lamda Function

l = lambda x: x * x
print(l(10))

list1=[1, 2, 3, 4, 5, 6]
# def even(x):
#     if x%2==0:
#         return x
# f = filter(even, list1)
f= filter(lambda x : x % 2 == 0, list1)
print(list(f))
