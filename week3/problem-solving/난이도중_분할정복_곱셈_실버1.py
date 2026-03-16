# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

A, B, C = list(map(int, input().split()))

result = 0

def partition(B):
    print(B)
    if (B == 0):
        return 1 % C
    elif (B == 1):
        print("B == 1")
        return A % C
    elif (B % 2 == 0):
        print("B % 2 == 0")
        half = partition(B//2)
        return (half * half) % C
    else:
        print("B % 2 != 0")
        half = partition(B//2)
        return A * (half * half) % C
    
result = partition(B)
print(result)