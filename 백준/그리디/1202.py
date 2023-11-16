# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-1202-%EB%B3%B4%EC%84%9D-%EB%8F%84%EB%91%91-Python
# https://bio-info.tistory.com/195

# N : 보석 개수
# M : 각 무게,   V : 각 가격
# K : 가방 개수,   C : 각 가방에 담을 수 있는 최대 무게
import heapq
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
jew = []
bags = []

for _ in range(n):
    heapq.heappush(jew, list(map(int, input().split())))

for _ in range(k):
    bags.append(int(input()))

jew.sort()
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)



