import sys
a = int(sys.stdin.readline().rstrip())
i = 0
d = []
while i < a:
    b,c = map(int, sys.stdin.readline().rstrip().split())
    d.append(b+c)
    i = i + 1

for j in range(a):
    print(f"Case #{j+1}: {d[j]}")