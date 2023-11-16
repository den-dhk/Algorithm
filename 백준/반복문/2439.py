import sys
a = int(sys.stdin.readline().rstrip())

for i in range(a):
    print(("*"*(i+1)).rjust(a))