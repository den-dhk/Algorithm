t = int(input())
result = []
# num = 1
for i in range(t):
    count = 0
    a = list(map(int, input().split()))
    for j in a:
        if j % 2 != 0:
            count = count + j
    result.append(count)
for i in range(t):
    print(f'#{i+1} {result[i]}')

# for i in result: 
#     print(f'#{num} {i}')
#     num += 1


'''
# 두 번째 풀이
t = int(input())

for i in range(t):
    sum = 0
    data = list(map(int, input().split()))
    for j in data:
        if j % 2 == 0:
            continue
        sum += j
    print(f'#{i+1} {sum}')
'''
