# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque

N, M, V = list(map(int, input().split()))

graph = {}

for i in range(N):
    graph[i+1] = []

for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in range(N):
    graph[i+1].sort()

print(graph)

DFS_result = []
def DFS(node):
    DFS_result.append(node)
    next_vertice = graph[node]
    for vertice in next_vertice:
        if vertice in DFS_result:
            continue
        DFS(vertice)
    
DFS(V)
print(" ".join(map(str, DFS_result)))

######################################

BFS_result = []
visited = []
queue = deque()
def BFS(node):
    BFS_result.append(node)
    visited.append(node)
    next_vertice = graph[node]
    for vertice in next_vertice:
        if vertice not in visited:
            visited.append(vertice)
            queue.append(vertice)
    while queue:
        node = queue.popleft()
        BFS_result.append(node)
        next_vertice = graph[node]
        for vertice in next_vertice:
            if vertice not in visited:
                visited.append(vertice)
                queue.append(vertice)
            

BFS(V)
print(" ".join(map(str, BFS_result)))