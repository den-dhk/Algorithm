machines = '0101'
start = 0
end = len(machines)-1
while start < end:
    if machines[end] == '0' and machines[start] == '1':
        k = []
        for i in range(len(machines)):
            k.append(machines[i])
        k[start], k[end] = k[end], k[start]
        machines = ''.join(k)
        start += 1
        end -= 1
    elif machines[end] == '0':
        start += 1
    elif machines[start] == '1':
        end -= 1
    else:
        start += 1
        end -= 1
print(machines)