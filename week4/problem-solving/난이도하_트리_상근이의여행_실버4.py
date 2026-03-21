# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 최악은 가야하는 나라 - 1
#  최선은? 
import sys
input = sys.stdin.readline

T = int(input())
answers = []

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        input()
    answers.append(str(N - 1))

sys.stdout.write("\n".join(answers))