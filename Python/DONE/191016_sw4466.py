import sys
sys.stdin = open('sw4466.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print('#%d %d' % (tc, sum(scores[:K])))
