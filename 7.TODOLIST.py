

'''

Input Format :
The first line of input will contain a single integer T, the number of test cases.
Then the testcases follow.
Each testcase consists of 2 lines of input.
The first line of input of each test case contains a single integer, N,
which is the total number of problems that the Chef has added to his to-do list.
The second line of input of each test case contains N space-separated integers D1,D2 ... DN
which are the difficulty ratings for each problem in the to-do list.

Output Format :
For each test case,
output in a single line the number of problems
that Chef will have to remove so that all remaining problems have a
difficulty rating strictly less than 1000.

'''

t = int(input())
for i in range(t):
    N = int(input())
    temp = list(map(str,input().split()))
    res = 0
    for i in temp:
        if int(i)>=1000:
            res+=1
    print(res)