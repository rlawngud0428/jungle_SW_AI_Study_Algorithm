# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

# 미로에서 이동할 때의 조건
# 1. 미로를 벗어나면 안됨 (0 <= i, j < N)
# 2. 미로의 해당 칸이 1 이어야 함 (그래야 이동가능)
# 3. 방문했던 곳은 다시 방문하지 않음 (visited)
import sys
input = sys.stdin.readline

from collections import deque

N, M = list(map(int, input().split()))

maze = []

# maze 입력받기
for i in range(N):
    col = input().strip()
    row = [int(row) for row in col]
    maze.append(row)

# 목적지 : maze[N-1][M-1]

# 스타트 : maze[0][0]

# 다음 가야할 곳
queue = deque()
queue.append((0,0))

# 좌표를 어차피 튜플로 전해줄거니까. 중복안되게 해서 있으면 스킵
visited = set()
visited.add((0,0))

depth = 0

ehckr = False

def ehckrF(i, j):
    global ehckr
    if (i,j) == (N-1, M-1):
        ehckr = True
        return True
    return False

while queue:
    depth += 1
    for _ in range(len(queue)):
        # i,j == 현재 보드의 좌표
        i, j = queue.popleft()
        visited.add((i,j))

        # 오른쪽 이동
        if j + 1 < M:
            if ehckrF(i, j+1):
                break
            if (maze[i][j+1] == 1 and (i, j+1) not in visited):
                visited.add((i, j+1))
                queue.append((i, j+1))
                

        # 아래쪽 이동
        if i + 1 < N:
            if ehckrF(i+1, j):
                break
            if (maze[i+1][j] == 1 and (i+1, j) not in visited):
                visited.add((i+1,j))
                queue.append((i+1, j))

        # 왼쪽 이동
        if j - 1 >= 0:
            if ehckrF(i, j-1):
                break
            if (maze[i][j-1] == 1 and (i, j-1) not in visited):
                visited.add((i, j-1))
                queue.append((i, j-1))

        # 위쪽 이동
        if i - 1 >= 0:
            if ehckrF(i-1, j):
                break
            if (maze[i-1][j] == 1 and (i-1, j) not in visited):
                visited.add((i-1, j))
                queue.append((i-1, j))
    if ehckr == True:
        break

print(depth+1)