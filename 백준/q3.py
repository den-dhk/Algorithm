start = [1,6,2,9]
end = [8,7,6,10]
n = 4
start.sort()
end.sort()
count = 0
result = 0
order = []
answer = 0
while len(end) != 0:
    if len(start) == 0:
        order.append((end.pop(0),0))
    elif start[0] <= end[0]:
        order.append((start.pop(0),1))
    else:
        order.append((end.pop(0), 0))
while len(order) != 0:
    x,y = order.pop(0)
    if y == 1:
        count += 1
    if y == 0:
        count -= 1
    if result < count:
        result = count
        answer = x

print(answer)