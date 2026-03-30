# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 지원자 수
    N = int(input())

    # 성적 입력 받음
    grade_arr = [tuple(map(int, input().split())) for _ in range(N)]
    # 성적 정렬 (첫번째 요소 기준)
    grade_arr.sort(key=lambda x : x[0])

    line = grade_arr[0][1]
    
    count = 1

    for grade in grade_arr[1:]:
        if grade[1] < line:
            count += 1
            line = grade[1]
    
    print(count)