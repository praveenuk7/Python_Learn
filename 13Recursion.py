def recursion(n):
    if n<=1:
        return n
    else:
        return n + recursion(n-1)
res=recursion(5)
print(res)

