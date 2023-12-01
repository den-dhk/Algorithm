# 해결 X

def solution(name):
    front = 0
    back = 0
    before = ["A" for _ in range(len(name))]
    a = ord(name[0]) - ord('A')
    b = ord('Z') - ord(name[0]) + 1
    front += min(a,b)
    back += min(a,b)
    before[0] = name[0]
    for i in range(1,len(name)):
        front += 1
        a = ord(name[i]) - ord('A')
        b = ord('Z') - ord(name[i]) + 1
        tmp = min(a,b)
        front += tmp
        before[i] = name[i]
        if ''.join(before) == name:
            break
    before = ["A" for _ in range(len(name))]
    before[0] = name[0]
    for i in range(len(name)-1,0,-1):
        back += 1
        a = ord(name[i]) - ord('A')
        b = ord('Z') - ord(name[i]) + 1
        tmp = min(a,b)
        back += tmp
        before[i] = name[i]
        if ''.join(before) == name:
            break
    answer = min(front,back)
    return answer
