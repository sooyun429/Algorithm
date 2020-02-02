import sys
sys.stdin = open('sw4698.txt', 'r')

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def favorite(n):
    global res, D
    while 1:
        if n % 10 == D:
            res += 1
            return
        if n // 10 == 0: return
        else: n //= 10


for tc in range(1, int(input())+1):
    D, A, B = map(int, input().split())
    res = 0
    if A <= prime[-1]:
        for p in prime:
            if p >= A and p <= B:
                favorite(p)
            if p > B:
                break
        A = prime[-1] + 1

    for i in range(A, B+1):
        for j in range(len(prime)):
            if prime[j] > i:
                break
            if prime[j] != i and (i % prime[j] == 0):
                break
            if prime[j] == i:
                favorite(i)
        else:
            prime += [i]
            favorite(i)

    print('#%d %d' % (tc, res))
