# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

# N = 물품의 수, K = 버틸 수 있는 무게 (제한사항)
N, K = list(map(int, input().split()))

item_list = []

for _ in range(N):
    W, V = list(map(int, input().split()))
    item_list.append((W, V))

# print(item_list)

value_arr = [0] * (K+1)

for item in item_list:
    # 큰 것부터 작은 순서로 해야지 중복사용이 없다.
    for idx in range(K, item[0]-1, -1):
        value_arr[idx] = max(value_arr[idx], value_arr[idx-item[0]] + item[1])

print(value_arr)
print(value_arr[K])