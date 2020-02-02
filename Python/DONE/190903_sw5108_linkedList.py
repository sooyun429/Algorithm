import sys
sys.stdin = open('sw5108.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    li = input().split()
    for i in range(M):
        idx, n = map(int, input().split())
        li = li[:idx] + [str(n)] + li[idx:]
    print('#%d %s' % (tc, li[L]))
