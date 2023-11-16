import sys

input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input())

count = 0
for word in words:
    dic = set([])
    tmp = True
    dic.add(word[0])
    for j in range(1,len(word)):
        if word[j] in dic and word[j] != word[j-1]:
            tmp = False
            break
        dic.add(word[j])
    if tmp is True:
        count += 1

print(count)