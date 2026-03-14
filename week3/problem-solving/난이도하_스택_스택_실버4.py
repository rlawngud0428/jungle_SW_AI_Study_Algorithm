# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def empty(self):
        if len(self.stack) == 0:
            return 1
        return 0
    
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
    
stack = Stack()

N = int(input())

result = []
for i in range(N):
    command = input()
    if "push" in command:
        command = command.split()
        stack.push(command[1])
    elif "pop" in command:
        result.append(stack.pop())
    elif "size" in command:
        result.append(stack.size())
    elif "empty" in command:
        result.append(stack.empty())
    elif "top" in command:
        result.append(stack.top())

for i in range(len(result)):
    print(result[i])