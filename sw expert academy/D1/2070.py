t = int(input())
result = []

for i in range(t):
    a,b = map(int, input().split())
    if a < b:
        result.append('<')
    elif a == b:
        result.append('=')
    else:
        result.append('>')

for i in range(t):
    print(f'#{i+1} {result[i]}')
