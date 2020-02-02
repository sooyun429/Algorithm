import sys
sys.stdin = open('sw5207.txt', 'r')


def binsearch(n, lst, part):  # part는 위치가 왼쪽인지, 오른쪽인지 구분하는 변수
    global result
    mid = (len(lst)-1)//2
    left = lst[:mid]
    right = lst[mid+1:]
    if part != 1:
        for i in left:
            if i == n:
                binsearch(n, left, 1)
    if part != 2:
        for i in right:
            if i == n:
                binsearch(n, right, 2)
    if n == lst[mid]:
        result += 1
        return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    result = 0
    for i in B:
        if i in A:
            binsearch(i, A, 0)
    print('#%d %d' % (tc, result))
