import sys
sys.stdin = open('DONE/sw1220.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for i in arr: print(i)
    # break

    