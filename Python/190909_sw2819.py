import sys
sys.stdin = open('sw2819.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    NN = [[0]*6] + [[0] + input().split() + [0] for _ in range(4)] + [[0]*6]
    for i in NN:
        print(i, end='\n')
    print('####')
    result = []
    for i in range(1, 5):
        for j in range(1, 5):
            temp = NN[i][j]
            stack = [NN[i][j]]
