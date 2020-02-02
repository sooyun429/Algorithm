import sys
sys.stdin = open('bj2628.txt', 'r')

W, H = map(int, input().split())
N = int(input())
cutting = [[0, H], [0, W]]
for i in range(N):
    a, b = map(int, input().split())
    cutting[a].append(b)
cutting[0].sort()
cutting[1].sort()
result = 0
for i in range(1, len(cutting[0])):
    for j in range(1, len(cutting[1])):
        temp = (cutting[0][i]-cutting[0][i-1])*(cutting[1][j]-cutting[1][j-1])
        if temp > result:
            result = temp
print(result)
