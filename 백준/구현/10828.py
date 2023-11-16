import sys
input = sys.stdin.readline
data = []
n = int(input())
for i in range(n):
    a = list(input().split())
    if a[0] == 'push':
        data.append(int(a[1]))
    elif a[0] == 'pop':
        print(data.pop() if len(data) != 0 else -1)
    elif a[0] == 'size':
        print(len(data))
    elif a[0] == 'empty':
        print(1 if len(data)==0  else 0)
    elif a[0] == 'top':
        print(data[-1] if len(data) != 0 else -1)