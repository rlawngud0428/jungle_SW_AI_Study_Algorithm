# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input())
seen = set()
result_idx = 0
result_char = ""

for i in range(N):
    str = input()
    temp = str[::-1]

    # 이 문장이 회문인지도 검사해야함.

    if str == temp:
        result_idx = len(temp)
        result_char = temp[result_idx//2]

    if temp in seen:
        result_idx = len(temp)
        result_char = temp[result_idx//2]
    seen.add(str)
        

print(result_idx, result_char)