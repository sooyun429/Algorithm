import sys
sys.stdin = open('sw3304_input.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = map(str, input().split())
    A = list(A)
    B = list(B)
    i = 0
    result_max = 0
    while i < len(A):
        count = 0
        for wb in B:
            if A[i] == wb:
                count += 1
                i += 1
            print(A[i], wb, count)
        if count > result_max:
            result_max = count
#        acaykp capcak
    print('#%d %d' % (tc+1, len(result_max)))
