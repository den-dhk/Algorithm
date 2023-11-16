import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
data = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in data:
    if binary_search(array, i, 0, n-1) != None:
        print(1)
    else:
        print(0)
