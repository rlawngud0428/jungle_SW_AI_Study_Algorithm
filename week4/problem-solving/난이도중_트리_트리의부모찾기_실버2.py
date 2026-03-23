# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

# u, v를 받았을 때 둘 중 하나는 이미 트리에 있어야 한다?
# 없으면 어떻게 해야하는가
# 보장이 되나? 무조건 이미 트리에 있는 정점들의 연결만 보여준다고

# 문제를 읽어볼 때는 안그런거 같은데
# 일단은 그렇다고 생각하고 문제풀이를 해야겠지?

# N = int(input())

# already_tree = set()
# already_tree.add(1)

# qnah_arr = [0] * (N + 1)

# for i in range(N-1):
#     u, v = list(map(int, input().split()))

#     if u in already_tree:
#         already_tree.add(v)
#         qnah_arr[v] = u
#     if v in already_tree:
#         already_tree.add(u)
#         qnah_arr[u] = v

# print(qnah_arr)

# 너무 양아치 스러운 접근이였구만

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

graph = {}

for i in range(N):
    graph[i+1] = []

for i in range(N-1):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
queue.append(1)

qnah_arr = [0] * (N+1)

while queue:
    node = queue.popleft()

    for idx in graph[node]:
        if qnah_arr[idx] != 0:
            continue
        qnah_arr[idx] = node
        queue.append(idx)

for i in range(N-1):
    print(qnah_arr[i+2])
