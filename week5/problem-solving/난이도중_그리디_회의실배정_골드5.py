# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

def select_meetings(meetings):
    if meetings is None:
        return 0
    pass

    meetings.sort(key=lambda x : (x[1], x[0]))
    
    selected = []
    selected.append(meetings[0])
    
    for meeting in meetings[1:]:
        if meeting[0] >= selected[-1][1]:
            selected.append(meeting)
    
    return len(selected)

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

result = select_meetings(meetings)
print(result)