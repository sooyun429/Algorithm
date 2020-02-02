import sys
sys.stdin = open('sw2005.txt', 'r')

def pascal_func(n):
    global pascal
    # if n == 1:
    #     print(pascal[n][0])
    #     return pascal[n]
    # else:
    if len(pascal)-1 < n:
        pascal = pascal + [[0] * (n - len(pascal) + 1)]
        temp = [1] + [0] * (n-2) + [1]
        for i in range(1, n-1):
            temp[i] = pascal[n-1][i-1] + pascal[n-1][i]
            pascal[n] = temp
    for i in pascal[1:n+1]:
        for j in i:
            print(str(j), end=' ')
        print('')
    return pascal[n]


T = int(input())
pascal = [[], [1], [1, 1], [1, 2, 1]]
for tc in range(1, T+1):
    N = int(input())
    print('#%d' % tc)
    pascal_func(N)
