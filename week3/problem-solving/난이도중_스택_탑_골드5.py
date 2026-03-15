# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

# 스택으로 뒤에서부터 계산. len(arr)
# next_tower = arr.pop()
# prev_tower = arr.pop()
# if next_tower > prev_tower:5
# for문 안에서 스택.pop을 하면 밖의 스택은 어떻게 되지?

N = int(input())

tower_list = list(map(int, input().split()))

# 이렇게 푸니까 시간초과 나옴.
# 접근 방식이 나쁘진 않았으나, 반대로 생각했으면 보다 더 시간을 줄일 수 있었을 것

# reversed_result = []

# while len(tower_list) != 1:
#     current_tower_idx = len(tower_list) - 1
#     current_tower = tower_list.pop()

#     target_tower_list = tower_list[::-1]
#     for i in target_tower_list:
#         if (i > current_tower):
#             reversed_result.append(current_tower_idx)
#             break
#         current_tower_idx -= 1
#         if (i == target_tower_list[-1]):
#             reversed_result.append(0)
        
    
# reversed_result.append(0)
# result = reversed_result[::-1]
# print(*result)

stack = []
result = [0] * N

for i in range(N):
    print(i)
    while stack and tower_list[stack[-1]] < tower_list[i]:
        print("while")
        stack.pop()

    if stack:
        print("if")
        result[i] = stack[-1] + 1
    
    print(result)

    stack.append(i)

print(*result)