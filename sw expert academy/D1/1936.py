a,b = map(int, input().split())

if a < b:
    if b == 3 and a == 1:
        print("A")
    else:
        print("B")
else:
    if a == 3 and b == 1:
        print("B")
    else:
        print("A")


'''
# 2회차
a,b = map(int, input().split())
a_win_list = [(1,3), (2,1), (3,2)]
if (a,b) in a_win_list:
    print('A')
else:
    print('B')
'''