import sys
sys.stdin = open('sw5205.txt', 'r')


def partition(l, r):
    global lst
    p = l
    i = l
    j = r
    while i < j:
        if lst[i] <= lst[p] and i < r:
            i += 1
        if lst[j] >= lst[p] and j > l:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def quickSort(l, r):
    global lst
    if l < r:
        m = partition(l, r)
        quickSort(l, m-1)
        # quickSort(m+1, r)
        if m < (N//2):
            quickSort(m + 1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quickSort(0, len(lst)-1)
    print('#%d %d' % (tc, lst[N//2]))
