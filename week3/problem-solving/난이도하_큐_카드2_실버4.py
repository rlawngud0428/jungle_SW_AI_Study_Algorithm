# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

# 역시나 그냥 풀면 시간초과가 뜬다

# N = int(input())
# num_list = [0] * N

# for i in range(N):
#     num_list[i] = (i+1)

# while len(num_list) != 1:
#     num_list.pop(0)
#     num = num_list.pop(0)
#     num_list.append(num)

# print(num_list[0])

from collections import deque

N = int(input())

queue = deque()
for i in range(N):
    queue.append(i+1)

while len(queue) != 1:
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue[0])