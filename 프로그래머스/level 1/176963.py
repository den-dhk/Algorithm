# 문제 이름 : 추억 점수
# name : 그리워하는 사람의 이름을 담은 문자열 배열
# yearning : 각 사람별 그리움 점수를 담은 정수 배열
# photo : 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열

def solution(name, yearning, photo):
    answer = []
    matching = dict(zip(name, yearning))
    for i in photo:
        hap = 0
        for j in i:
            if j in name:
                hap += matching[j]
        answer.append(hap)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))