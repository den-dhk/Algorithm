# 이해 X
t = int(input())
result = []
for tc in range(t):
    n, k = map(int, input().split())
    student = []
    grade = [''] * n
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for j in range(n):
        middle, final, homework = map(int, input().split())
        score = middle * 0.35 + final * 0.45 + homework * 0.2
        student.append((j, score))
    student.sort(key=lambda x: x[1], reverse=True)

    for j in range(1, 11):
        for x in range(n//10*(j-1), n//10*j):
            grade[student[x][0]] = grades[j-1]
    result.append(grade[k-1])

for i in range(t):
    print('#{} {}'.format((i+1), result[i]))


'''
# 2회차
t = int(input())

score_table = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1,t+1):
    n,k = map(int, input().split())
    result = []
    for i in range(n):
        mid, fin, hom = map(int, input().split())
        score = mid*0.35 + fin*0.45 + hom*0.2
        result.append((score, i+1))
    result.sort(key=lambda x: -x[0])
    a = n // 10
    for i in range(n):
        if k == result[i][1]:
            print(f'#{tc} {score_table[i//a]}')
'''