t = int(input())
a = list(map(int, input().split()))
if t != len(a):
    print("개수 오류")

a.sort()
i = int(len(a) / 2)
print(a[i])