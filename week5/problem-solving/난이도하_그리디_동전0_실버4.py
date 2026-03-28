# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

N, K = list(map(int, input().split()))

coins = []

for i in range(N):
    coins.append(int(input()))

reversed_coins = reversed(coins)

result = 0

for coin in reversed_coins:
    if K == 0:
        break
    count = K // coin
    K = K % coin
    result += count

print(result)