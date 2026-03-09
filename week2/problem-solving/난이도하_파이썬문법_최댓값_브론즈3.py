# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

num_list = []

for i in range(9):
    num_list.append(int(input()))
   
print(max(num_list))
print(num_list.index(max(num_list))+1)