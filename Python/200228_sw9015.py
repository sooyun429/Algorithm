import sys
sys.stdin = open('sw9015.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    division = 1
    status = 0
    idx = 1

    while idx < N:
        if status == 0:
            if numbers[idx] > numbers[idx-1]:
                status = 1
            elif numbers[idx] < numbers[idx-1]:
                status = -1
        elif numbers[idx] == numbers[idx-1]:
            status = 0
        elif (status == 1 & numbers[idx] < numbers[idx-1]) or (status == -1 & numbers[idx] > numbers[idx-1]):
            status = 0
            division += 1
        idx += 1
    
    print('#%d %d' % (tc, division))

