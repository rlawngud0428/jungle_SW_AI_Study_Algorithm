# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

def cal_diff(num_arr):
    diff = 0
    for i in range(len(num_arr) - 1):
        diff += abs(num_arr[i] - num_arr[i+1])
    return diff

N = int(input())

num_list = list(map(int, input().split()))

checked = []
used = [False] * N
result = 0

def backtrack():
    global result
    if len(checked) == N:
        value = cal_diff(checked)
        if value > result:
            result = value
        return
    
    for i in range(N):
        if used[i]:
            continue

        used[i] = True
        checked.append(num_list[i])
        backtrack()
        checked.pop()
        used[i] = False

backtrack()
print(result)
