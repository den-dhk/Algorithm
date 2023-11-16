n = int(input())
n = 1000 - n
option = [500,100,50,10,5,1]
count = 0
for i in option:
    count += n // i
    n %= i

print(count)