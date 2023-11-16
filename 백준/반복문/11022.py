import sys
a = int(sys.stdin.readline().rstrip())
i = 0
d = []
e = []
f = []

while i < a:
    b,c = map(int, sys.stdin.readline().rstrip().split())
    e.append(b)
    f.append(c)
    d.append(b+c)
    i = i + 1

for j in range(a):
    print(f"Case #{j+1}: {e[j]} + {f[j]} = {d[j]}")