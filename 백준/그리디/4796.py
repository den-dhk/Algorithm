result = []

while True:
    index = 1
    l,p,v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    a = (v // p) * l
    a += v % p if v%p <= l else l
    result.append(a)

for i in range(len(result)):
    print(f'Case {i+1}: {result[i]}')