import sys
sys.stdin = open('sw1232.txt', 'r')

def cal(n):
    if edges[n][1] + edges[n][2] == 0:
        return edges[n][0]
    else:
        if edges[n][0] == '-':
            return cal(edges[n][1]) - cal(edges[n][2])
        elif edges[n][0] == '+':
            return cal(edges[n][1]) + cal(edges[n][2])
        if edges[n][0] == '*':
            return cal(edges[n][1]) * cal(edges[n][2])
        if edges[n][0] == '/':
            return cal(edges[n][1]) / cal(edges[n][2])

for tc in range(1, 11):
    N = int(input())
    edges = [[0, 0, 0] for _ in range(N+1)]
    for i in range(N):
        temp = list(map(str, input().split()))
        if len(temp) == 4:
            edges[int(temp[0])] = [temp[1], int(temp[2]), int(temp[3])]
        elif len(temp) == 2:
            edges[int(temp[0])] = [int(temp[1]), 0, 0]
        else:
            print('edge case')
    print('#%d %d' % (tc, int(cal(1))))
