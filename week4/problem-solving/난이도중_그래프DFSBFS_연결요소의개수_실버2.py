# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

# DFS 풀이방법

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M = list(map(int, input().split()))

# graph = {}

# for i in range(N):
#     graph[i+1] = []

# for _ in range(M):
#     u, v = list(map(int, input().split()))
#     graph[u].append(v)
#     graph[v].append(u)

# def DFS(node):
#     visited.add(node)
#     next_node = graph[node]
#     for node in next_node:
#         if node in visited:
#             continue
#         DFS(node)

# visited = set()
# result = 0

# for i in range(1, N+1):
#     if i in visited:
#         continue
#     DFS(i)
#     result += 1

# print(result)



# BFS 풀이방법

# from collections import deque
# import sys
# input = sys.stdin.readline

# N, M = list(map(int, input().split()))

# graph = {}

# for i in range(N):
#     graph[i+1] = []

# for _ in range(M):
#     u, v = list(map(int, input().split()))
#     graph[u].append(v)
#     graph[v].append(u)

# visited = set()
# result = 0

# for i in range(1, N+1):
#     if i in visited:
#         continue

#     queue = deque([i])
#     visited.add(i)

#     while queue:
#         node = queue.popleft()
#         for nxt in graph[node]:
#             if nxt in visited:
#                 continue
#             visited.add(nxt)
#             queue.append(nxt)

#     result += 1

# print(result)

# 스택 DFS (반복문 DFS)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}
for i in range(N):
    graph[i+1] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()
result = 0

for i in range(1, N+1):
    if i in visited:
        continue

    stack = [i]
    visited.add(i)

    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if nxt in visited:
                continue
            visited.add(nxt)
            stack.append(nxt)

    result += 1

print(result)