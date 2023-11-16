n,k = map(int, input().split())
data = [i for i in range(1,n+1)]
result = []
index = (k-1)
while data:
    a = data.pop(index)
    result.append(a)
    if not data:
        break
    index = (index + (k-1)) % len(data)

print('<', ', '.join(str(i) for i in result), '>', sep='')
# sep : 구분자