import sys
sys.stdin = open('sw4843_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    result = ''
    for i in range(5):
        result += ' ' + str(numbers[-1-i]) + ' ' + str(numbers[i])
    print('#{}{}'.format(tc+1, result))