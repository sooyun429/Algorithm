import sys
sys.stdin = open('sw5201.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)
    moved = [0]*len(w)
    result = 0

    for i in range(len(t)):
        if sum(moved) == N:
            break
        for j in range(len(w)):
            if t[i] >= w[j] and not moved[j]:
                result += w[j]
                moved[j] = 1
                break
    print('#%d %d' % (tc, result))
