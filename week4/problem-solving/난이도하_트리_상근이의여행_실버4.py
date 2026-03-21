# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 최악은 가야하는 나라 - 1
#  최선은? 
result = []

T = int(input())

for i in range(T):
    N, M = list(map(int, input().split()))
    for i in range(M):
        u, v = list(map(int, input().split()))
    result.append(N-1)

for res in result:
    print(res)