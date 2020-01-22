import sys
sys.stdin = open('bj1120.txt', 'r')

words = list(map(str, input().split()))
A, B = len(words[0]), len(words[1])
res = A
for i in range(0, B-A+1):
    temp = 0
    for j in range(0, A):
        if words[0][j] != words[1][i+j]:
            temp += 1
    if temp < res: res = temp

print(res)

