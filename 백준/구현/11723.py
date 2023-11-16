m = int(input())
result = set([])
for i in range(m):
    a = input().split()
    if a[0] == 'add':
        result.add(int(a[1]))
    if a[0] == 'remove':
        result.remove(int(a[1]))
    if a[0] == 'check':
        if int(a[1]) in result:
            print(1)
        else:
            print(0)
    if a[0] == 'toggle':
        if int(a[1]) in result:
            result.remove(int(a[1]))
        else:
            result.add(int(a[1]))
    if a[0] == 'all':
        result = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    if a[0] == 'empty':
        result = set([])
    if a[0] == 'print':
        print(result)
    