def findMax(list):
    max=list[0]
    for item in list:
        if item>max:
            max=item
    return max

def findMin(list):
    min=list[0]
    for item in list:
        if item<min:
            min=item
    return min
