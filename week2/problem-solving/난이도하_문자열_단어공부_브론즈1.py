# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

str = input().upper()
A = 65
alphaList = [0 for i in range(26)]

for i in range(len(str)):
	idx = ord(str[i]) - A
	alphaList[idx] += 1

maxValue = max(alphaList)
if (alphaList.count(maxValue) > 1):
	print("?")
else:
	print(chr(alphaList.index(maxValue) + A))