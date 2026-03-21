# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# 2개면 걍 쭈우우우우욱 연결
# 3개면 1개 이후 분열해서 또 쭈우우우욱
# n-1개면 걍 게ㅔㅔㅔㅔ속 분열
# N개의 정점과 M개의 리프가 있다는 거니까.
# 둘 사이의 관계를 나타낸다면.

# 결론적으로 리프가 몇개냐에 따라 완전 달라지는 느낌이네 

N, M = list(map(int, input().split()))


result = []

for i in range(N-1):
    if (i <= N - M):
        result.append([i, i+1])
    else:
        result.append([N-M, i+1])

for i in result:
    print(" ".join(map(str, i)))