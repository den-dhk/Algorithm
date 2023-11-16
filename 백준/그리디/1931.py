# https://suri78.tistory.com/26

n = int(input())
data = []

for i in range(n):
    a,b = map(int, input().split())
    data.append((a,b))

data.sort(key=lambda x: (x[1],x[0]))
cnt = 1
end_time = data[0][1]
for i in range(1,n):
    if data[i][0] >= end_time:
        cnt += 1
        end_time = data[i][1]

print(cnt)