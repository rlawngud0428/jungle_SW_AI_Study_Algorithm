# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys
input = sys.stdin.readline

from collections import deque

N, M = list(map(int, input().split()))

hazard = set(int(input()) for _ in range(M))


def dp(i, j):
    if N == 1:
        return 0
    
    if 2 in hazard:
        return -1
    
    queue = deque()
    counted = set()
    
    queue.append((i, j, 1))
    counted.add((i, j))

    while queue:
        i, j, cnt = queue.popleft()

        if (i == N):
            return cnt
        
        if (i in hazard):
            continue

        if j - 1 > 0:
            next_i = i + j - 1
            next_j = j - 1
            if next_i <= N and next_i not in hazard and (next_i, next_j) not in counted:
                queue.append((next_i, next_j, cnt + 1))
                counted.add((next_i, next_j))

        next_i = i + j
        next_j = j
        if next_i <= N and next_i not in hazard and (next_i, next_j) not in counted:
            queue.append((next_i, next_j, cnt + 1))
            counted.add((next_i, next_j))

        next_i = i + j + 1
        next_j = j + 1
        if next_i <= N and next_i not in hazard and (next_i, next_j) not in counted:
            queue.append((next_i, next_j, cnt + 1))
            counted.add((next_i, next_j))
    
    return -1
    
result = dp(2, 1)
print(result)