# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.cursor = self.head
    
    def append(self, data):
        new_node = Node(data)

        last = self.tail.prev
        last.next = new_node
        new_node.prev = last

        new_node.next = self.tail
        self.tail.prev = new_node

        self.cursor = new_node

    def move_left(self):
        if self.cursor != self.head:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor.next != self.tail:
            self.cursor = self.cursor.next

    def insert(self, data):
        new_node = Node(data)
        right = self.cursor.next

        self.cursor.next = new_node
        new_node.prev = self.cursor

        new_node.next = right
        right.prev = new_node

        self.cursor = new_node

    def delete_left(self):
        if self.cursor == self.head:
            return
        
        deleted = self.cursor
        left_node = deleted.prev
        right_node = deleted.next

        left_node.next = right_node
        right_node.prev = left_node

        self.cursor = left_node
    
    def get_text(self):
        result = []
        current = self.head.next

        while current != self.tail:
            result.append(current.data)
            current = current.next

        return "".join(result)
    
text = input().strip()
editor = DoublyLinkedList()

for char in text:
    editor.append(char)

N = int(input())

for i in range(N):
    command = input().split()

    if command[0] == "L":
        editor.move_left()
    elif command[0] == "D":
        editor.move_right()
    elif command[0] == "B":
        editor.delete_left()
    elif command[0] == "P":
        editor.insert(command[1])

print(editor.get_text())
