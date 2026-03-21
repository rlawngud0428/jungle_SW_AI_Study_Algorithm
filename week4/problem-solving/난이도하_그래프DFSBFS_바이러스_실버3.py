# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 우선 그래프가 있어야함.
# 그리고 그 그래프에 리스트로 초기화 해야함
# 무방향 그래프라고 보는게 맞는 듯 함
# infected = [] 만들어서 사실상의 visited로 쓰자.
# 예를 들어 1번이 감염되었다고 하면,
# 1번의 간선 즉 다음 노드들을 전부 queue에다가 넣고
# 1번은 infected에 append.
# 이걸 게ㅔㅔㅔ속 반복
# 마지막에 len(infected)

from collections import deque

graph = {}

N = int(input())
M = int(input())

# 1번부터 N까지
for i in range(N):
    graph[i+1] = []

# 그래프 연결
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

infected = set()

next_infected = deque()
next_infected.append(1)

while next_infected:
    infected_com = next_infected.popleft()
    infected.add(infected_com)

    next_com = graph[infected_com]
    for i in next_com:
        if i in infected:
            continue
        next_infected.append(i)

print(len(infected) - 1)