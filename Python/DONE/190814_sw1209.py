import sys
sys.stdin = open('sw1209_input.txt', 'r')

for _ in range(1, 11):
    T = int(input())
    box = [0] * 100
    max_sum = 0
    for i in range(100):
        box[i] = (list(map(int, input().split())))
        if max_sum < sum(box[i]):
            max_sum = sum(box[i])

    for y in range(100):
        comparison = 0
        for x in range(100):
            comparison += box[x][y]
        if comparison > max_sum:
            max_sum = comparison

    comparison1 = comparison2 = 0
    for s in range(100):
        comparison1 += box[s][s]  # 대각선 정방향의 합
        comparison2 += box[s][99 - s]  # 대각선 역방향의 합
    if comparison1 > max_sum:
        max_sum = comparison1
    if comparison2 > max_sum:
        max_sum = comparison2

    print('#%d %d' % (T, max_sum))