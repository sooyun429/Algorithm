import sys
sys.stdin = open('bj2116.txt', 'r')

N = int(input())
dices = [0]*N

for i in range(N):
    dices[i] = list(map(int, input().split()))

print(dices)