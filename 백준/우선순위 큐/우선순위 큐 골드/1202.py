import sys
import heapq
input = sys.stdin.readline

n,k = map(int, input().split())
jew = []
bags = []
for i in range(n):
    m,v = map(int, input().split())
    heapq.heappush(jew, ((m,v)))
for i in range(k):
    bags.append(int(input()))
bags.sort()

answer = 0
tmp = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jew)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jew:
        break
print(answer)