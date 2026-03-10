# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

N = int(input())

def N_Queen(N):
    cols = [0] * N
    result = 0

    def backtrack(rows):
        nonlocal result

        if (rows == N):
            result += 1
            return
        
        for col in range(N):
            possible = True

            for row in range(rows):
                if cols[row] == col:
                    possible = False
                    break
                if abs(rows - row) == abs(col - cols[row]):
                    possible = False
                    break
            if not possible:
                continue
            
            cols[rows] = col
            backtrack(rows + 1)

    backtrack(0)
    return result

print(N_Queen(N))