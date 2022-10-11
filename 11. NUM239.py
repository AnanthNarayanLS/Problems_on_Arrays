
'''

Vasya likes the number 239.
Therefore, he considers a number pretty
if its last digit is 2, 3 or 9.

Vasya wants to watch the numbers between LL and RR (both inclusive),
so he asked you to determine how many pretty numbers are in this range.

Input :
The first line of the input contains a single integer T denoting the number of test cases.
The description of TT test cases follows.
The first and only line of each test case contains two space-separated integers L and R.

Output :
For each test case,
print a single line containing one integer — the number of pretty numbers between LL and RR.

'''

t = int(input())
for i in range(t):
    count = 0
    l,r = map(int , input().split())
    for i in range(l,r+1):
        if (i%10==2 or i%10==3 or i%10==9):
            count+=1
    print(count)