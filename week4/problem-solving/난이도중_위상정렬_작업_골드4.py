# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

import sys
input = sys.stdin.readline

N = int(input())

graphs = {}

for i in range(N):
    inputs = list(map(int, input().strip().split()))

    graphs[i+1] = {"time" : inputs[0], "edges": [], "prev": []}
    if inputs[1] == 0:
        continue
    else:
        for idx in range(2, inputs[1]+2):
            graphs[inputs[idx]]["edges"].append(i+1)
            graphs[i+1]["prev"].append(inputs[idx])

empty_edges_graph = {k: v for k, v in graphs.items() if not v["edges"]}

memo = {}

# dfs로 max time 구하기
def dfs(node):
    if node in memo:
        return memo[node]
    if not graphs[node]["prev"]:
        memo[node] = graphs[node]["time"]
        return memo[node]

    memo[node] = graphs[node]["time"] + max(dfs(prev) for prev in graphs[node]["prev"])
    return memo[node]

result = 0
for node in empty_edges_graph:
    temp = dfs(node)
    result = max(result, temp)

print(result)