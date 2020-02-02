## quick sort

## 연습문제 1
## 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오.


def partition(lst, l, r):
    p = lst[l]
    i = l
    j = r
    while i <= j:
        while lst[i] <= p and i < r:
            i += 1
        while lst[j] >= p and j > l:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def quickSort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quickSort(lst, l, s-1)
        quickSort(lst, s+1, r)

a = [11, 45, 23, 81, 28, 34]
b = [11, 45, 22, 81, 23, 34, 99, 17, 8]
c = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

quickSort(a, 0, len(a)-1)
print(a)

