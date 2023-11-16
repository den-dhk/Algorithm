from bisect import bisect_left, bisect_right

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
data = list(map(int, input().split()))

for i in data:
    print((bisect_right(array, i) - bisect_left(array,i)), end= ' ')

