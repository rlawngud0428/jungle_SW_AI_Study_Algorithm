# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

def is_prime(num):
    if (num < 2):
        return 0
    if (num == 2):
        return 1
    if (num % 2 == 0):
        return 0
    i = 3
    while i*i <= num:
        if (num % i == 0):
            return 0
        i += 2
    return 1

N = int(input())
num_list = list(map(int, input().split()))
result = 0

for num in num_list:
    result += is_prime(num)

print(result)