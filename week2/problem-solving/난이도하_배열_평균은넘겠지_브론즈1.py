# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

def get_avg(scores):
    total = scores[0]
    sum = 0
    for i in range(1, len(scores)):
        sum += scores[i]
    return sum / total

def get_percent(avg, scores):
    total = scores[0]
    above = 0
    for i in range(1, total+1):
        if (scores[i] > avg):
            above += 1
    percent = (above / total) * 100
    return f"{percent:.3f}%"

C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    avg = get_avg(scores)
    print(get_percent(avg, scores))