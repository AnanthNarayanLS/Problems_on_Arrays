

#Given an array A of size N of integers.
# Your task is to find the minimum and maximum elements in the array.

def getMinMax(a, n):
    min=a[0]
    max=a[0]
    i=1
    for i in range(n):
        if a[i]<min:
            min=a[i]
        if a[i]>max:
            max=a[i]
    return min, max

print(getMinMax([2,22,1,4,33],5))