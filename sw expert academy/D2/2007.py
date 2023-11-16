# 사실상 못풀었음
t = int(input())
result = []

def length_find(pattern):
    answer = 1
    for i in range(1,11):
        if pattern[0:i] == pattern[i:i+i]:
            answer = i
            break
    return answer


for i in range(t):
    a = str(input())
    result.append(length_find(a))

for i in range(t):
    print(f'#{i+1} {result[i]}')


'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    s = input()
    result = 0
    for i in range(1,11):
        if s[:i] == s[i:i+i]:
            result = i
            break
    print(f'#{tc} {result}')
'''