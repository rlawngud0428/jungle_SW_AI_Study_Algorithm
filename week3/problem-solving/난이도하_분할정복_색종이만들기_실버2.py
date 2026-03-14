# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def square(x, y, size):
    global white, blue

    first_color = paper[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != first_color:
                half = size // 2
                
                square(x, y, half)
                square(x+half, y, half)
                square(x, y+half, half)
                square(x+half, y+half, half)
                return
            
    if first_color == 0:
        white += 1
    else:
        blue += 1

square(0,0,N)

print(white)
print(blue)