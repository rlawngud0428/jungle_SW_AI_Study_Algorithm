# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

N = int(input())

memo = {}

memo[0] = 1
memo[1] = 2

for i in range(2, N):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746 

result = memo[N-1]
print(result)