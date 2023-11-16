n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
total = 0

for i in range(n-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    
    total += min_cost * distance[i]

print(total)

'''
# 틀림, 서브테스크 1개 맞춤 => 너무 조건 많이 달아서 그런듯
# n = int(input())
# distance = list(map(int, input().split()))
# cost = list(map(int, input().split()))

# result = cost[n-2] * distance[n-2]
# min_cost = cost[n-2]
# total_distance = distance[n-2]
# if n == 2:
#     print(result)
# else:
#     for i in range(n-3,-1,-1):
#         total_distance += distance[i]
#         if cost[i] < min_cost:
#             result = cost[i] * total_distance
#         else:
#             result += cost[i] * distance[i]

# print(result)
'''