n = 4
m = 3
# song_preferences = [[0,1,3,2], [0,2,3,1], [1,0,3,2], [2,1,0,3], [0,3,1,2]]
song_preferences = [[2,0,1], [0,2,1], [0,1,2], [2,1,0]]
d = [0] * m
for i in range(n):
    for j in range(m-1):
        d[song_preferences[i][j]] += m-j-1
result = []
for i in range(m):
    result.append((d[i],i))
# key=lambda x: (-x[0], x[1])
result.sort(reverse=True)
print(result)
for i in result:
    print(i[1])