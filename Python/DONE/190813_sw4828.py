import sys
sys.stdin = open('sw4828_input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#%d %d' % (i+1, max(numbers)-min(numbers)))
