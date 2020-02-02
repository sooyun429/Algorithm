import sys
sys.stdin = open('sw1242.txt', 'r')

T = int(input())
code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(1, T+1):
    N, M = map(int, input().split())
    NN = [list(input()) for _ in range(N)]
