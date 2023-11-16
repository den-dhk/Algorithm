import sys
input = sys.stdin.readline().strip

x = int(input())
index = 1
k = 0
while k < x:
    k += index
    if k >= x:
        k -= index
        break
    index += 1
order = x - k
if index % 2 == 0:
    m = order
    n = index - order + 1
    print(f'{m}/{n}')
else:
    m = index - order + 1
    n = order
    print(f'{m}/{n}')


