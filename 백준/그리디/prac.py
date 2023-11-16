n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
left_d = 0   # 앞의 d 변수 저장
data = []   # d,p 튜플로 묶어서 리스트에 저장

# 첫 번째 주유소 두번째 주유소 사이는 무조건 첫번 째 주유소에서 충전하고 가야됨
result = p[0] * d[0]

for i in range(1, n-1):
    data.append((p[i], d[i], i))     # (가격, 거리, 순서)의 튜플로 묶어서 data에 저장

data = sorted(data, key=lambda x: x[0])     # 가격 순으로 정렬
result += (data[0][0] * data[0][1])          # 가장 가격 낮은 곳 기준
o_standard = data[0][2]                     # 순서 기준점
p_standard = data[0][0]                     # 가격 기준점(최저 가격)

for i in range(1, len(data)):
    if data[i][2] > o_standard:             # 순서가 뒤일 경우
        result += (p_standard * data[i][1]) # 같은 가격에 거리만 곱해서 더해줌
    else:
        a = sum(d[data[i][2]:o_standard])   # 지금 순서에서 원래 순서까지의 거리를 합산
        result += (data[i][0] * a)          # 가격과 곱해서 result에 더해줌
        o_standard = data[i][2]             # 순서 기준점 변경
        a = 0
print(result)
    