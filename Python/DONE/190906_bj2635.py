import sys
sys.stdin = open('bj2635.txt', 'r')

N = int(input())
maxresult = [2, 0]
for i in range(N, -1, -1):
    result = [N, i]
    while result[-2]-result[-1] >= 0:
        result.append(result[-2]-result[-1])
    if len(result) > maxresult[0]:
        maxresult[0] = len(result)
        maxresult[1] = result
print(maxresult[0])
for i in maxresult[1]:
    print(i, end=' ')
