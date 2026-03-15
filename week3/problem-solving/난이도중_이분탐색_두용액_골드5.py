# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

N = int(input())

value_list = list(map(int, input().split()))
min_value = float('inf')
results = [0] * 2

# for i in range(len(value_list)-1):
#     for j in range(i+1, len(value_list)):
#         value = abs(value_list[i] + value_list[j])
#         if value < min_value:
#             min_value = value
#             result[0] = value_list[i]
#             result[1] = value_list[j]

# print(result[0], result[1])

# 이게 왜 이분탐색 문제인거지..?
# 그야 수가 존나 크니까 그렇지 좌식아

# 굳이 이분탐색인가?
# 그럴 필요가 없다~
# 우리의 친구 two pointer가 있다~

value_list.sort()


# 일단 이분탐색으로 풀어볼까?
# right - left == 1 이라면,
# target 값은 없는 상황이니까, left의 값과 target 비교, right의 값과 target 비교, 최소값을 찾아서 갱신

# arr[mid] == target : 그냥 정답이므로 반환 ㅋㅋ

# 근데 생각해보니까 갱신할 때 흐음.. 기존의 선택했던 값들을 넣어줘야 한다는 점이 문제긴 하네

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1

    if left == 0:
        return 0
    elif left == len(arr):
        return len(arr) - 1
    else:
        if abs(arr[left - 1] - target) <= abs(arr[left] - target):
            return left - 1
        else:
            return left
    

for i in range(len(value_list)):
    target = - value_list[i]
    idx = binary_search(value_list, target)
    
    if idx != i:
        value = abs(abs(value_list[i] + value_list[idx]))
        if value < min_value:
            min_value = value
            results[0] = value_list[i]
            results[1] = value_list[idx]

results.sort()
print(results[0], results[1])