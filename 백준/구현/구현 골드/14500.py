# 이해 X
import sys
input = sys.stdin.readline

move = [(0,1), (0,-1), (1,0), (-1,0)]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

maxValue = 0

def dfs(i,j,dsum,cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return
    
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]