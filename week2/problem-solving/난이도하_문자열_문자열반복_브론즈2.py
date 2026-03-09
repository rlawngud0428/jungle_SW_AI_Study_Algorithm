# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

T = int(input())
i = 0
while (i < T):
	R, S = map(str, input().split(' '))
	result = ''
	for j in range(len(S)):
		result += S[j]*int(R)
		j+=1
	print(result)
	i+=1