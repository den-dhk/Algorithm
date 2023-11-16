h,m = map(int, input().split())
c = int(input())
if m + c >= 60:
  if h + ((m+c) // 60) >= 24: 
    h = h + ((m+c) // 60) - 24
    m = (m + c) % 60 
    print(h, m)
  else:
    h = h + ((m+c) // 60)
    m = (m + c) % 60
    print(h, m)
else:
  m = m + c
  print(h, m)
