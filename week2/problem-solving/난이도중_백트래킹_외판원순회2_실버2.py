# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

N = int(input())
cost_arr = []

result = float('inf')

for i in range(N):
    cost_arr.append(list(map(int, input().split())))

visited = []

def backtrack(now, next, cost):
    global result

    if len(visited) == N and cost_arr[now][visited[0]] != 0:
        total = cost + cost_arr[now][visited[0]]
        if total < result:
            result = total
        return
    
    for next in range(N):
        if next not in visited and cost_arr[now][next] != 0:
            visited.append(next)
            backtrack(next, next, cost+cost_arr[now][next])
            visited.pop()

visited.append(0)
backtrack(0,0,0)

print(result)

# 아래 방식은 코스트를 너무 많이 씀

# def backtrack():
    
#     if len(visited) == N:
#         for i in range(N):
#             print(cost_arr[visited[i-1]][visited[i]])
#         return

#     for i in range(N):
#         if i in visited:
#             continue

#         visited.append(i)
#         backtrack()
#         visited.pop()