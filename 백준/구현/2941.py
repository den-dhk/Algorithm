# import sys
# input = sys.stdin.readline

c_alphabet = ['c=',  'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
fa = ['c', 'd', 'l', 'n', 's', 'z']

s = input()

count = 0
i = 0
while i <= len(s)-1:
    if s[i] == 'd':
        if s[i:i+3] == 'dz=':
            i += 3
            count += 1
            continue
    elif s[i] in fa:
        if s[i:i+2] in c_alphabet:
            i += 2
            count += 1
            continue
    i += 1
    count += 1
print(count)

# s = 'ddz=z='
# s = 'ljes=njak'