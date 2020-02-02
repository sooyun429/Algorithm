import sys
sys.stdin = open('sw4831_input.txt', 'r')

T = int(input())
for i in range(T):
    K, N, M = map(int, input().split())  # 3 10 5
    bus_stop = list(map(int, input().split()))  ## 1 3 5 7 9
    count = 0
    location = 0
    move = K
    while location + move < N:
        if location + move in bus_stop:
            location += move
            count += 1
            move = K
        else:
            move -= 1
            if move == 0:
                count = 0
                break

    print('#%d %d' % (i+1, count))
