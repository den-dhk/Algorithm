s = int(input())
cnt = 0
i = 1
while True:
    if i > s:
        break
    s -= i
    cnt += 1
    i += 1

print(cnt)