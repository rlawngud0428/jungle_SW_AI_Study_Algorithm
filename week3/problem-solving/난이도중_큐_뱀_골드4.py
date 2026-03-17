# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

# is_crashed_by_wall (함수)
    # 벽의 길이가 N으로 정해졌으니, 이동했는데, 보드의 끝을 넘어서면 game_over return time
# is_crashed_by_self (자기자신이라, 걍 큐랑 set으로)
    # 내 몸을 큐로 받고 append
    # 충돌 확인 혹은 꼬리 이동 시에는 tail = deque.popleft() 가장 왼쪽값. (꼬리의 위치)
    # 꼬리 즉 충돌을 확인할 때는 set을 이용하므로 remove를 사용하면 됨 (어차피 값은 있을거니까.) 값 추가는 add

# is_turn_left
    # (x,y) x 증가(왼쪽으로 이동중) -> y 증가 / x 감소 -> y 감소
    # (x,y) y 증가 (위쪽으로 이동중) -> x 감소 / y 감소 -> x 증가
# is_turn_right
    # (x,y) x 증가 -> y 감소 / x 감소 -> y 증가
    # (x,y) y 증가 -> x 증가 / y 감소 -> x 증가

# while True로 돌리는게 가장 현명한가??
# 그 안에서 타임은 i += 1로 계산하고?

from collections import deque

# 보드게임 길이
N = int(input())

# 사과 갯수
apple_num = int(input())

# 사과 위치 리스트
apple_list = set()
for i in range(apple_num):
    x, y = map(int, input().split())
    apple_list.add((x-1, y-1))

# 명령 갯수
order_num = int(input())

# 명령 위치 리스트
order_list = dict()
for i in range(order_num):
    time, command = input().split()
    order_list[int(time)] = command

snake_body = deque([(0, 0)])
check_snake_body = {(0, 0)}

# dir은 무조건 0-3이 나온다.
# 그래서 방향 인덱스 사용하는 것도 낫베드 하다.
# dx[dir] dy[dir]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

time = 0

while True:
    time += 1

    head_x, head_y = snake_body[-1]
    nx = head_x + dx[dir]
    ny = head_y + dy[dir]

    # 벽 충돌
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        print(time)
        break
    
    # 자기 몸 충돌
    if (nx, ny) in check_snake_body:
        print(time)
        break

    #  사과 먹었을 때
    if (nx, ny) in apple_list:
        apple_list.remove((nx, ny))
    # 사과 안먹었을 때
    else:
        tail = snake_body.popleft()
        check_snake_body.remove(tail)

    # 몸 추가
    snake_body.append((nx, ny))
    check_snake_body.add((nx, ny))

    # 방향 전환
    if time in order_list:
        if order_list[time] == "D":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4
