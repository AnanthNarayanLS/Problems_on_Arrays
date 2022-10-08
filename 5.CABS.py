

'''

Problem
Chef has to travel to another place.
For this, he can avail any one of two cab services.
The first cab service charges X rupees.
The second cab service charges Y rupees.
Chef wants to spend the minimum amount of money.
Which cab service should Chef take?

Input Format
The first line will contain T - the number of test cases.
Then the test cases follow.
The first and only line of each test case contains two integers
X and Y - the prices of first and second cab services respectively.

Output Format
For each test case,
output FIRST if the first cab service is cheaper,
output SECOND if the second cab service is cheaper,
output ANY if both cab services have the same price.

You may print each character of
FIRST, SECOND and ANY in uppercase or lowercase
(for example, any, aNy, Any will be considered identical).

'''

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a==b:
        print("any")
    elif a<b:
        print("first")
    else:
        print("second")