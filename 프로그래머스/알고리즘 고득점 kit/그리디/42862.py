# n : 전체 학생수
# lost : 체육복 도난당한 학생 번호
# reserve : 여벌 가져온 학생 번호

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    
    for i in reserve:
        if i in lost or (i+1) in lost or (i-1) in lost:
            if i in lost:
                lost.remove(i)
            elif (i-1) in lost:
                lost.remove(i-1)
            elif (i+1) in lost:
                lost.remove(i+1)
    answer = n-len(lost)
    return answer