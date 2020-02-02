import sys
sys.stdin = open('sw5204.txt', 'r')


def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = mergesort(lst[:mid])
        right = mergesort(lst[mid:])
        return merge(left, right)
    else:
        return lst


def merge(left, right):
    global cnt, lst
    i = 0
    j = 0
    arr = []
    if left[-1] > right[-1]:
        cnt += 1
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while (i<len(left)):
        arr.append(left[i])
        i += 1
    while (j<len(right)):
        arr.append(right[j])
        j += 1
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = mergesort(lst)
    print('#%d %d %d' % (tc, lst[N//2], cnt))
