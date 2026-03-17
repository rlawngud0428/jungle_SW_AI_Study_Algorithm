# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

# 이중연결리스트
# append 하는 타이밍이 중요해보임.
# 그리고 폐쇄는 2개역 이상일때만 가능한게 당연한거긴 하지
# 그리고 걍 진행상황 result에 저장했다가 출력하기
# 흠 간단해보이는데, 아닌가?
# 아닐수도?

# 아래 풀이는 시간초과가 나옴.
# 당연하지 ㅄ아. 누가 이따구로 코드짜냐 제정신이냐??

# 딕셔너리를 이용해서 문제를 풀면 풀릴까

# 다행이다. 딕셔너리를 넣어도 어차피 안되는 거였다.

# import sys
# input = sys.stdin.readline

# result = []

# station_table = dict()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = Node(None)
#         self.tail = Node(None)

#         self.head.next = self.tail
#         self.head.prev = self.tail
#         self.tail.prev = self.head
#         self.tail.next = self.head
    
#     def append(self, data):
#         new_node = Node(data)
#         station_table.update({data : new_node})

#         last = self.tail.prev
#         last.next = new_node
#         new_node.prev = last

#         new_node.next = self.tail
#         self.tail.prev = new_node

#     def insert_prev(self, station, data):
#         new_node = Node(data)
#         station_table.update({data: new_node})
#         current = station_table[station]
#         current_prev = current.prev
#         if current_prev == self.head:
#             result.append(self.tail.prev.data)
#         else:
#             result.append(current_prev.data)

#         new_node.next = current_prev.next
#         new_node.prev = current.prev
#         current.prev = new_node
#         current_prev.next = new_node
    
#     def insert_next(self, station, data):
#         new_node = Node(data)
#         station_table.update({data: new_node})
#         current = station_table[station]
#         current_next = current.next
#         if current_next == self.tail:
#             result.append(self.head.next.data)
#         else:
#             result.append(current_next.data)

#         new_node.next = current.next
#         new_node.prev = current_next.prev
#         current.next = new_node
#         current_next.prev = new_node

#     def delete_prev(self, station):
#         deleted = station_table[station].prev
#         if deleted == self.head:
#             deleted = self.tail.prev
#             deleted.prev.next = deleted.next
#         else:
#             deleted.prev.next = deleted.next
#             deleted.next.prev = deleted.prev
#         result.append(deleted.data)
#         del station_table[deleted.data]

#     def delete_next(self, station):
#         deleted = station_table[station].next
#         if deleted == self.tail:
#             deleted = self.head.next
#             deleted.next.prev = deleted.prev
#         else:
#             deleted.prev.next = deleted.next
#             deleted.next.prev = deleted.prev
#         result.append(deleted.data)
#         del station_table[deleted.data]

#     # def get_where(self, target):
#     #     current = self.head.next

#     #     while current != self.tail:
#     #         if current.data == target:
#     #             return current
#     #         current = current.next      

# N, M = list(map(int, input().split()))

# subway = DoublyLinkedList()

# prev_subway_map = list(map(int, input().split()))

# for i in prev_subway_map:
#     subway.append(i)

# print(station_table)

# for i in range(M):
#     command = input().split()

#     if command[0] == "BP":
#         subway.insert_prev(int(command[1]), int(command[2]))
#     elif command[0] == "BN":
#         subway.insert_next(int(command[1]), int(command[2]))
#     elif command[0] == "CP":
#         subway.delete_prev(int(command[1]))
#     elif command[0] == "CN":
#         subway.delete_next(int(command[1]))

# print(station_table)
# for i in result:
#     print(i)

# 이렇게 작성해도 시간초과 뜸
# ㄹㅇ 너무 개같음
# 온갖 잡기술을 다 써야함

# N, M = list(map(int, input().split()))

# stations = list(map(int, input().split()))

# max = 1000001

# prev = [0] * max
# next = [0] * max

# for i in range(N):
#     prev[stations[i]] = stations[i-1]
#     next[stations[i-1]] = stations[i]

# result = []

# for i in range(M):
#     command = input().split()

#     if command[0] == "BP":
#         i = int(command[1])
#         j = int(command[2])
#         prev_station = prev[i]
#         result.append(prev_station)

#         next[prev_station] = j
#         prev[j] = prev_station
#         next[j] = i
#         prev[i] = j

#     elif command[0] == "BN":
#         i = int(command[1])
#         j = int(command[2])
#         next_station = next[i]
#         result.append(next_station)

#         next[i] = j
#         prev[j] = i
#         next[j] = next_station
#         prev[next_station] = j
        
#     elif command[0] == "CP":
#         i = int(command[1])

#         target = prev[i]
#         result.append(target)

#         prev_station = prev[target]
#         prev[i] = prev_station
#         next[prev_station] = i

        
#     elif command[0] == "CN":
#         i = int(command[1])

#         target = next[i]
#         result.append(target)

#         next_station = next[target]
#         next[i] = next_station
#         prev[next_station] = i

# for i in result:
#     print(i)

# 결국 gpt 와의 합작으로 나온 코드
# 진심 너무 화가 나는 코드이다.

import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

N = int(next(it))
M = int(next(it))

stations = [int(next(it)) for _ in range(N)]

MAX = 1000001

prev = [0] * MAX
next_ = [0] * MAX

for i in range(N):
    prev[stations[i]] = stations[i - 1]
    next_[stations[i - 1]] = stations[i]

result = []

for _ in range(M):
    cmd = next(it)

    if cmd == b'BP':
        i = int(next(it))
        j = int(next(it))
        prev_station = prev[i]
        result.append(str(prev_station))

        next_[prev_station] = j
        prev[j] = prev_station
        next_[j] = i
        prev[i] = j

    elif cmd == b'BN':
        i = int(next(it))
        j = int(next(it))
        next_station = next_[i]
        result.append(str(next_station))

        next_[i] = j
        prev[j] = i
        next_[j] = next_station
        prev[next_station] = j

    elif cmd == b'CP':
        i = int(next(it))

        target = prev[i]
        result.append(str(target))

        prev_station = prev[target]
        prev[i] = prev_station
        next_[prev_station] = i

    else:  # CN
        i = int(next(it))

        target = next_[i]
        result.append(str(target))

        next_station = next_[target]
        next_[i] = next_station
        prev[next_station] = i

sys.stdout.write('\n'.join(map(str, result)))