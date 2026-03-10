# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
import math

C = int(input())

N = [int(input()) for i in range(C)]

def is_prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

for num in N:
    target = int(num // 2)
    left = target
    right = target

    if is_prime(target):
        print(target, target)
        continue
    
    diff = 1
    while True:
        left = target - diff
        right = target + diff
        if (is_prime(left) and is_prime(right)):
            print(left, right)
            break
        diff += 1