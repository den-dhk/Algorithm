import heapq
import sys
input = sys.stdin.readline

leftheap = []
rightheap = []
n = int(input())
for i in range(n):
    x = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -x)
    else:
        heapq.heappush(rightheap, x)
    
    if rightheap and rightheap[0] < -leftheap[0]:
        leftValue = heapq.heappop(leftheap)
        rightValue = heapq.heappop(rightheap)

        heapq.heappush(leftheap, -rightValue)
        heapq.heappush(rightheap, -leftValue)
    
    print(-leftheap[0])

