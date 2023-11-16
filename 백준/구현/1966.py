import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    q = deque(list(map(int, input().split())))
    s = max(q)
    result = []
    order = 0
    index = m
    while q:
        if q[0] < s:
            if index == 0:
                index = len(q)-1
            else:
                index -= 1
            k = q.popleft()
            q.append(k)
            
        else:
            if index == 0:
                order += 1
                break
            k = q.popleft()
            result.append(k)
            order += 1
            index -= 1
            s = max(q)
    print(order)


