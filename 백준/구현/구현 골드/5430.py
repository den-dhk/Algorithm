from collections import deque

t = int(input())

for _ in range(t):
    p = input()  # 명령
    n = int(input()) # 배열 수 개수
    s_data = input() # 배열
    data = deque(s_data[1:-1].split(','))
    error = False
    order = 0   # 순서
    for i in p:
        if i == 'R':
            order += 1 
        if i == 'D':
            if n == 0:
                error = True
                break
            if order % 2 == 0:
                data.popleft()
            else:
                data.pop()
            n -= 1
    if not error:
        if order % 2 == 0:
            print('[', ','.join(i for i in data), ']', sep='')
        else:
            print('[', ','.join(data[i] for i in range(len(data)-1, -1,-1)), ']', sep='')
    else:
        print('error')



'''
# 무조건 덱을 써야만 풀리는 문제인가...?
# import sys

# input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input()  # 명령
    n = int(input()) # 배열 수 개수
    s_data = input() # 배열
    data = []
    for i in s_data:
        if i.isdigit():
            data.append(i)
    error = False
    order = 0   # 순서
    for i in p:
        if i == 'R':
            order += 1 
        if i == 'D':
            if n == 0:
                error = True
                break
            if order % 2 == 0:
                data.pop(0)
            else:
                data.pop()
            n -= 1
    if not error:
        if order % 2 == 0:
            print('[', ','.join(i for i in data), ']', sep='')
        else:
            print('[', ','.join(data[i] for i in range(len(data)-1, -1,-1)), ']', sep='')
    else:
        print('error')
'''