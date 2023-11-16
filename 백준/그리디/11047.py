# n : 동전의 종류   k : 가치의 합
n,k = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
start_point = 0
result = 0

for i in range(len(data)):
    if i > k:
        break
    start_point = i

for j in range(i, -1, -1):
    if k == 0:
        break
    result += k // data[j]
    k %= data[j]

print(result)

'''
# 두 번째 풀이
n,k = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)
count = 0
index = 0
while k != 0:
    count += k // data[index]
    k = k % data[index]
    index += 1

print(count)
'''