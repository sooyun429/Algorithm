import sys
sys.stdin = open('sw1493.txt', 'r')

T = int(input())
dots = [[0, 0] for _ in range(100000)]
cnt = 1
for i in range(1, 301):
    for j in range(1, i+1):
        dots[cnt] = [j, i+1-j]
        cnt += 1

for tc in range(1, T+1):
    p, q = map(int, input().split())
    answer = [dots[p][0]+dots[q][0], dots[p][1]+dots[q][1]]
    print('#%d %d' % (tc, dots.index(answer)))

