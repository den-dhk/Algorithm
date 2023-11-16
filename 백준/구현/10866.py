from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
result = deque([])
for _ in range(n):
    k = input().split()
    if k[0] == 'push_front':
        result.appendleft(k[1])
    elif k[0] == 'push_back':
        result.append(k[1])
    elif k[0] == 'pop_front':
        print(result.popleft() if len(result) != 0 else -1)
    elif k[0] == 'pop_back':
        print(result.pop() if len(result) != 0 else -1)
    elif k[0] == 'size':
        print(len(result))
    elif k[0] == 'empty':
        print(1 if len(result) == 0 else 0)
    elif k[0] == 'front':
        print(result[0] if len(result) != 0 else -1)
    elif k[0] == 'back':
        print(result[-1] if len(result) != 0 else -1)