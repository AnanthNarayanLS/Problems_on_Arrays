



def rev1(arr , n):
    return arr[::-1]

def rev2(arr , n):
    temp = arr
    i = 0
    j = n-1
    while(i<j):
        temp[i],temp[j] = temp[j],temp[i]
        i+=1
        j-=1
    return temp


arr = [1,2,3,4,5]

print(rev1(arr,5))
print(rev2(arr,5))