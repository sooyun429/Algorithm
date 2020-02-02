import sys
sys.stdin = open('sw5203.txt', 'r')

def babygin(lst):
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            if lst[i] == lst[j] and lst[j] == lst[j+1]:
                return 1
            if lst[j]-lst[i] == 1:
                for k in range(j+1, len(lst)):
                    if lst[k]-lst[j] == 1:
                        return 1


T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    p1 = num[::2]
    p2 = num[1::2]
    result = 0
    for i in range(3, 7):
        temp1 = p1[:i]
        temp2 = p2[:i]
        temp1.sort()
        if babygin(temp1):
            result = 1
            break
        temp2.sort()
        if babygin(temp2):
            result = 2
            break
    print('#%d %d' % (tc, result))
