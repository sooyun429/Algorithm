import sys
sys.stdin = open('sw4835_input.txt', 'r')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    add = []
    for j in range(N-M+1):
        add.append(sum(numbers[j:j+M]))
    print('#%d %d' % (i+1, max(add)-min(add)))
