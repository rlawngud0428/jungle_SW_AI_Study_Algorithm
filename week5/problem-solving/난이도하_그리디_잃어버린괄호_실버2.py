# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

line = input()

line_splited_minus = line.split("-")

result = []

for i in line_splited_minus:
    i = list(map(int, i.split("+")))
    temp = 0
    for x in i:
        temp += x
    result.append(temp)

answer = 0

for j in result:
    answer -= j

answer += result[0]*2

print(answer)