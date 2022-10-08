
'''

Input
An integer t, 1<=t<=100,
denoting the number of testcases,
followed by t lines,
each containing a single integer n, 1<=n<=100.

Output
For each integer n given at input,
display a line with the value of n!

'''


def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

t=int(input())
for i in range(t):
    num=int(input())
    print(factorial(num))