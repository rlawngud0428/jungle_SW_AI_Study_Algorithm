# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

input1 = input()
input2 = input()

n = len(input1)
m = len(input2)

# 하나도 선택 안했을 때 -> 마지막 요소까지
LCS_count = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if input1[i-1] == input2[j-1]:
            LCS_count[i][j] = LCS_count[i-1][j-1] + 1
        else:
            LCS_count[i][j] = max(LCS_count[i-1][j], LCS_count[i][j-1])

print(LCS_count[n][m])