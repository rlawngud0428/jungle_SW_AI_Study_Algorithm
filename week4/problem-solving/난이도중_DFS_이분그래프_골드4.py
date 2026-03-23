# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    # 정점의 개수, 간선의 개수
    V, E = map(int, input().split())
    # 그래프 초기화
    graph = {}
    for i in range(V):
        graph[i+1] = []
    # 간선에 대한 정보 삽입
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append((v))
        graph[v].append((u))
    # 색깔 배열 초기화
    color = [0] * (V+1)
    result = "YES"

    queue = deque()

    for i in range(1, V+1):
        if color[i] != 0:
            continue

        color[i] = 1

        queue.append(i)

        while queue and result == "YES":
            node = queue.popleft()
            edges = graph[node]
            
            for edge in edges:
                if color[edge] != 0:
                    if color[edge] == color[node]:
                        result = "NO"
                        break
                else:
                    color[edge] = -color[node]
                    queue.append(edge)
        
        if result == "NO":
            break

    print(result)