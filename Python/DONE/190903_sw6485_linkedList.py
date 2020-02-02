import sys
sys.stdin = open('sw6485.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus_stop[j] += 1
    P = int(input())
    result = ''
    for i in range(P):
        C = int(input())
        result += ' ' + str(bus_stop[C])
    print('#%d%s' % (tc, result))
