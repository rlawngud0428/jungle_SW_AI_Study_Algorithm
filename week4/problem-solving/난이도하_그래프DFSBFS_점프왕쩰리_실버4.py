# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 문제 완벽 이해
# 지금 밟고 있는 발판의 숫자만큼 이동해야함.
#   -> 숫자가 N보다 크다면 사망
# DFS, BFS 라는디.. 왜지..?
# 살짝 백트래킹 느낌 나는 문제인디

# 노드 left, right 대신에 down, right 이느낌으로
# 안에 조건문으로 크기 넘어가면 바로 return
# 아니라면 그 그래프 내에서 다시 down, right

from collections import deque

# 게임 구역의 크기 2 <= N <= 3
N = int(input())

# 2차원 리스트로 보드
board = []

# 방문한 노드에 대해 다시 방문 X
visited = []
next_node = deque()

result = "Hing"

# board에 이동거리 입력
for i in range(N):
    board.append(list(map(int, input().split())))

# 현재의 위치 (i, j)
# 현재의 위치를 visited에 append
# 다음에 가야하는 node를 next_node에 append
def move(i, j):
    global result
    if i >= N or j >= N:
        return
    if (i, j) in visited:
        return
    visited.append((i, j))
    distance = board[i][j]

    if distance == -1:
        result = "HaruHaru"
    next_node.append((i+distance, j))
    next_node.append((i, j+distance))

next_node.append((0,0))

while next_node:
    i, j = map(int, next_node.popleft())
    move(i, j)

print(result)