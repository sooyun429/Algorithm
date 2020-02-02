import sys
sys.stdin = open('input.txt', 'r')

for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    count = 0
    while count < dump:
        boxes[-1] -= 1
        boxes[0] += 1
        count += 1
        boxes.sort()
    print('#%d %d' % (i, boxes[-1]-boxes[0]))

