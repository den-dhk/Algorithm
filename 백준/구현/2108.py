import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    num = int(input())
    data.append(num)
data.sort()
cnt = Counter(data).most_common(2)

print(round(sum(data)/len(data)))
print(data[len(data) // 2])

if len(data) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])   
print(max(data) - min(data))
