s = input()
c0 = 0
c1 = 0
if s[0] == '0':
    c0 += 1
else:
    c1 += 1

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            c0 += 1
        else:
            c1 += 1
print(min(c0,c1))