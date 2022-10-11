
'''

Given a list of N contest codes,
where each contest code is either START38 or LTIME108,
count how many problems were featured in each of the contests.

Input Format :
First line will contain TT, number of test cases.
Then the test cases follow.
Each test case contains of two lines of input.
First line of input contains
the total count of problems that appeared in the two recent contests - N.
Second line of input contains
the list of NN contest codes.
Each code is either START38 or LTIME108, to which each problem belongs.

Output Format :
For each test case,
output two integers in a single new line -
the first integer should be the number of problems in START38, and the
second integer should be the number of problems in LTIME108.

'''

t = int(input())

for i in range(t):
    n_count = int(input())
    n_code = list(input().split())
    start_count = 0
    ltime_count = 0
    for i in n_code:
        if i=='START38':
            start_count+=1
        else:
            ltime_count+=1
    print(f"{start_count} {ltime_count}")