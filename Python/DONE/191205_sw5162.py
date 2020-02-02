import sys
sys.stdin = open('sw5162.txt', 'r')

for tc in range(1, int(input())+1):
    A, B, C = map(int, input().split())
    if A < B:
        res = C//A
    else:
        res = C//B
    print('#%d %d' % (tc, res))