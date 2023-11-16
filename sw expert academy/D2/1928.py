# https://velog.io/@boggy/Python-Base64-Decoder-Encoder-import-%EC%97%86%EC%9D%B4
# 라이브러리 사용 : https://swbeginner.tistory.com/entry/SWEA-%EC%BD%94%EB%94%A9-Base64-Decoder-PYTHON-1928

t = int(input())

for tc in range(1,t+1):
    text = input()
    table = {s: i for i,s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
    bit_pattern = ''.join([bin(table[s])[2:].zfill(6) for s in text])
    text = ''.join([chr(int(bit_pattern[i:i+8],2)) for i in range(0,len(bit_pattern), 8)])
    print(f'#{tc} {text}')
