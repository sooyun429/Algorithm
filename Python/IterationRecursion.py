def Recursion(A):
    n = len(A)
    min = 0
    if n > 1:
        for i in range(1, n):
            if A[min] > A[i]:
                min = i
        A[0], A[min] = A[min], A[0]
        print(A)
        A = [A[0]] + Recursion(A[1:])
    else:
        return A


def rec_SelectionSort(A, s, e):
    if s == e: return

    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j

    A[s], A[mini] = A[mini], A[s]
    rec_SelectionSort(A, s+1, e)


def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]



test = [3, 2, 5, 1, 2, 9, 10]
# SelectionSort(test)
# print(test)
# Recursion(test)
# print(test)
rec_SelectionSort(test, 0, len(test)-1)
print(test)