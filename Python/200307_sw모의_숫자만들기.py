import sys
sys.stdin = open('sw숫자만들기.txt', 'r')

import itertools

for tc in range(1, int(input()+1)):
    N = int(input())
    operators = input().split()
    numbers = list(map(int, input().split()))
    

