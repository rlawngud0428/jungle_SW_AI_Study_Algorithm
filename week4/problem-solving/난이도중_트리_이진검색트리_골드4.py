# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 전위 순회는 살짝 DFS로 풀면 될거 같고,
# 그렇게 만들어진 graph에다가
# 후위 순회는 BFS 느낌으로 풀면 될거 같은데...
# 접근법을 이렇게 잡는게 맞나?
# 다른 방법이 뭐가 있을까...

# 플래그를 stack으로 쌓으면 좀 구별이 될거 같기도 하고
# 넣어두고 비교해서 간다? 이런 마인드?

# 일단 트리 만들 때는 Stack으로 해서 트리 구현하고,
# 후위 순회 결과를 어떻게 뽑아내지?

# visited 쓰고, 만약 left, right가 None or in visited 이라면 print
# 이런 식으로 하면 될거같네

# 내 생각
# 1. stack을 활용하여, 일단 이진검색트리를 만든다.
# 2. 재귀를 활용하여, 후위순회 결과를 출력한다.
# 3. 되겠지 뭐

# 끝이 있는 입력인데, 끝을 몰라. 그럼 어떻게 입력을 받지?
# -> https://pchild.tistory.com/2
# 킹갓 import sys, sys.stdin>readlines()

import sys
nums = [TreeNode(int(x.strip())) for x in sys.stdin.readlines()]

savedNode = nums[0]
stack = [savedNode]

for node in nums[1:]:
    # 스택이 빈 상황 (처음)
    if stack == []:
        stack.append(node)
        continue
    
    prev = stack[-1]
    # 이전의 값과 비교해서 값이 작은 상황
    if node.value < prev.value:
        prev.left = node
        stack.append(node)
        continue

    parent = None
    while stack and stack[-1].value < node.value:
        parent = stack.pop()

    parent.right = node
    stack.append(node)

result = []

def dfs(node):
    if node is None:
        return
    dfs(node.left)
    dfs(node.right)
    result.append(node.value)

dfs(savedNode)
print(savedNode.left)
print(result)