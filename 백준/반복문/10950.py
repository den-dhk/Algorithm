a = int(input())
n = 0
d =[]
while n < a:
    b,c = map(int, input().split())
    d.append(b+c)
    n = n + 1

for i in range(a):
    print(d[i])