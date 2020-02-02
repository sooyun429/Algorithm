import sys
sys.stdin = open('sw3975.txt', 'r')

# print 실행속도를 줄이는 방법
T = int(input())
result = [0]*(T+1)
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    A, B = a/b, c/d
    if A>B:
        result[tc] = '#%d ALICE' % tc
    elif A==B:
        result[tc] = '#%d DRAW' % tc
    else:
        result[tc] = '#%d BOB' % tc
print('\n'.join(result[1:]))



# T = int(input())
# for tc in range(1, T+1):
#     a, b, c, d = map(int, input().split())
#     if a/b > c/d:
#         result = 'ALICE'
#     elif a/b == c/d:
#         result = 'DRAW'
#     else:
#         result = 'BOB'
#     print('#%d %s' % (tc, result))
