# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

N = int(input())

num_list = set()
for _ in range(N):
    num_list.add(int(input()))

sum_2_list = set()

for i in num_list:
    for j in num_list:
        sum_2_list.add(i + j)

result = 0

for i in num_list:
    for j in num_list:
        if (i - j) in sum_2_list:
            if (i > result):
                result = i

print(result)