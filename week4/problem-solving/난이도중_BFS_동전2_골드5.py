# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

# import sys
# input = sys.stdin.readline

# from collections import deque

# N, K = list(map(int, input().split()))

# penny_list = []

# for _ in range(N):
#     penny_list.append(int(input()))

# penny_list.sort()

# global result
# result = float('inf')

# for i in reversed(penny_list):
#     queue = deque()
#     total = 0
#     depth = 0
#     queue.append((i, total))

#     while queue:
#         depth += 1

#         if depth > result:
#             break

#         for _ in range(len(queue)):
#             penny, total = queue.popleft()
#             total += penny

#             if total > K:
#                 continue

#             if total == K:
#                 result = min(result, depth)
#                 continue

#             for i in reversed(penny_list):
#                 queue.append((i, total))
# print(result)

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

penny_list = []

for _ in range(N):
    penny_list.append(int(input()))

# 중복 제거
penny_list = list(set(penny_list))

# 이미 만들어본 금액
already_counted = set()

queue = deque()
queue.append((0, 0))   # (현재 금액, 사용한 동전 개수)
already_counted.add(0)

while queue:
    total, cnt = queue.popleft()

    if total == K:
        print(cnt)
        break

    for penny in penny_list:
        nxt = total + penny

        if nxt <= K and nxt not in already_counted:
            already_counted.add(nxt)
            queue.append((nxt, cnt + 1))
else:
    print(-1)