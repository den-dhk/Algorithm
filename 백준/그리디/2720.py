t = int(input())
data = [25,10,5,1]
result = []

for i in range(t):
    p = int(input())
    a = p // data[0]
    p %= data[0]
    b = p // data[1]
    p %= data[1]
    c = p // data[2]
    p %= data[2]
    d = p
    result.append((a,b,c,d))

for i in result:
    print(i[0],i[1],i[2],i[3])