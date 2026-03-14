# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

N = int(input())
num_list = list(map(int, input().split()))

M = int(input())
test_num_list = list(map(int, input().split()))

results = [0] * M 

# for i in range(M):
#     for num in num_list:
#         if (test_num_list[i] == num):
#             results[i] = 1
#             break

# for result in results:
#     print(result)

num_list.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == target):
            return 1
        
        if (arr[mid] <= target):
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

for i in range(M):
    results[i] = binary_search(num_list, test_num_list[i])

for result in results:
    print(result)