# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

def m4l(addr_list):
    for i in range(len(addr_list)):
        addr_list[i] = addr_list[i].zfill(4)
        full_addr.append(addr_list[i])

def make_addr(addr_list):
    result = ""
    for i in range(len(addr_list)-2):
        addr_list[i] += ":"
        result += addr_list[i]
    print(result)

addr = input()

if "::" in addr:
    full_addr = []
    result = ""
    left, right = addr.split("::")
    left = left.split(":")
    right = right.split(":")
    makeMore = 8 - (len(left) + len(right))
    more = ["0"]*makeMore

    m4l(left)
    m4l(more)
    m4l(right)
    
    # full_addr에 다 있음
    # 이제 :만 추가하면 됨
    for i in range(len(full_addr)-1):
        full_addr[i] = (full_addr[i] + ":")
    
    for i in range(len(full_addr)):
        result += full_addr[i]
    
    print(result)

else:
    full_addr = []
    result = ""
    all_addr = addr.split(":")
    m4l(all_addr)
    for i in range(len(all_addr)-1):
        all_addr[i] = (all_addr[i] + ":")
    
    for i in range(len(all_addr)):
        result += all_addr[i]
    
    print(result)
    
