

'''

Input :

The first line of the input will contain
a single integer N (N ≤ 10000)
indicating the number of rounds in the game.
Lines 2,3,...,N+1 describe the scores of the two players in the N rounds.
Line i+1 contains two integer Si and Ti,
the scores of the Player 1 and 2 respectively, in round i.
You may assume that 1 ≤ Si ≤ 1000 and 1 ≤ Ti ≤ 1000.

NOTE :
'' at the end of each round,
the cumulative score for each player is calculated,
and the leader and her current lead are found.
Once all the rounds are over
the player who had the maximum lead at the end of any round
in the game is declared the winner. ''

Output :

Your output must consist of a single line
containing two integers W and L,
where W is 1 or 2 and indicates the winner and
L is the maximum lead attained by the winner.

'''

n = int(input())
p_1_score = 0
p_2_score = 0
lead = 0
for i in range(n):
    p_1,p_2 = map(int,input().split())
    p_1_score = p_1_score + p_1
    p_2_score = p_2_score + p_2
    diff = p_1_score - p_2_score
    if diff > 0 and diff > lead:
        lead = diff
        leader = 1
    elif diff < 0  and abs(diff) > lead:
        lead = abs(diff)
        leader = 2
print(leader,lead)