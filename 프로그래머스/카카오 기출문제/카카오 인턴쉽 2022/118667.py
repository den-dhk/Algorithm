from collections import deque

def solution(queue1, queue2):
    c = len(queue1)
    m1 = max(queue1)
    m2 = max(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    sum_value = s1 + s2
    max_value = max(m1, m2)
    if sum_value - max_value < max_value or sum_value % 2 != 0:
        return -1
    result = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    count = 0
    while s1 != s2:
        if count > c * 4:
            return -1
        if s1 > s2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            s1 -= tmp
            s2 += tmp
            result += 1
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            s2 -= tmp
            s1 += tmp
            result += 1
        count += 1
    return result

# 4n 길이 조건 참조했음 : https://simsim231.tistory.com/273