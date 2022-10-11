
'''

Problem
Chef has an array A of length N.

In one operation,
Chef can choose any two distinct indices i,j (1≤i,j≤N,i!=j)
and either change A_i to A_j
or change A_j to A_i
Find the minimum number of operations required
to make all the elements of the array equal.

Input Format :
First line will contain TT, number of test cases.
Then the test cases follow.
First line of each test case consists of an integer N - denoting the size of array A.
Second line of each test case consists of N space-separated integers A_1, A_2, ....... , A_N
denoting the array AA.

Output Format :
For each test case,
output the minimum number of operations required to make all the elements equal.

'''

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in arr:
        if arr.count(i) > count :
            count = arr.count(i)
    res = n - count
    print(res)
