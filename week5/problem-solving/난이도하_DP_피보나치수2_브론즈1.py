# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())

def fibo_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    memo[0] = 0
    memo[1] = 1

    if n in memo:
        return memo[n]

    memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)

    return memo[n]

result = fibo_memo(n)
print(result)