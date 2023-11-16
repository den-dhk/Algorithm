import sys
a = int(sys.stdin.readline().rstrip())
i = 0
d = []
while i < a:
    b,c = map(int, sys.stdin.readline().split())
    d.append(b+c)
    i = i + 1

for n in range(a):
    print(d[n])