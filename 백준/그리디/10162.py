t = int(input())
data = [300, 60, 10]
a = t // data[0]
t %= data[0]
b = t // data[1]
t %= data[1]
c = t // data[2]
t %= data[2]
if t != 0:
    print(-1)
else:
    print(a, b, c)