
'''

Problem :
Given the list of numbers,
you are to sort them in non decreasing order.

Input :
t – the number of numbers in list, then t lines follow [t <= 10^6].
Each line contains one integer: N [0 <= N <= 10^6]

Output :
Output given numbers in non decreasing order.

'''

lis=[]
t=int(input())
while t>0:
    n=int(input())
    lis.append(n)
    t-=1
lis.sort()
for i in range(0,len(lis)):
    print(lis[i])
