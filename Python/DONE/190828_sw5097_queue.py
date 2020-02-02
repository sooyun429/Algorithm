import sys
sys.stdin = open('sw5097.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, turn = map(int, input().split())
    numbers = input().split()
    print('#%d %s' % (tc, numbers[turn%N]))