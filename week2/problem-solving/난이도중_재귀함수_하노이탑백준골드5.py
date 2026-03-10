# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

N = int(input())

def move(N, x, y):
    if (N > 1):
        move(N-1, x, 6-x-y)
    print(x, y)
    if (N > 1):
        move(N-1, 6-x-y, y)

print(2**N - 1)
if (N <= 20):
    move(N, 1, 3)