import sys
sys.stdin = open('200129_naver ai burningday_04.txt', 'r')

# # 현지 문제 풀이
# def solution(A, B):
#     num = A*B
#     n = bin(num)
#     n = n[2:]
#     result = n.count('1')
#     return result

A, B = map(int, input().split())
num = A*B
n = bin(num) # 0b10101  bin 함수를 사용하면 접두어가 붙는다.
# 2진수: 0b (bin)
# 8진수: 0o  (oct)
# 16진수: 0x  (hex)
n = n[2:]
result = n.count('1')
print(result)