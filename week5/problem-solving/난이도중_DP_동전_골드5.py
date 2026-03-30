# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    value_arr = [0] * (target+1)
    
    for coin in coins:
        for idx in range(1, target+1):
            if idx + coin <= target:
                value_arr[idx+coin] += value_arr[idx]
            if idx % coin == 0:
                value_arr[idx] += 1

    print(value_arr[-1])
