import sys
sys.stdin = open('sw4839_input.txt', 'r')

def binarySearch(pages, start, end, S, cnt):
    middle = (start + end) // 2
    if S == pages[middle-1]:
        return cnt + 1
    elif S < pages[middle-1]:
        return binarySearch(pages, start, middle, S, cnt + 1)
    elif S > pages[middle-1]:
        return binarySearch(pages, middle, end, S, cnt + 1)


T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, input().split())  # 400 300 350
    start = 1
    end = P
    pages = list(range(1, P + 1))
    Pa_count = binarySearch(pages, start, end, Pa, 0)
    Pb_count = binarySearch(pages, start, end, Pb, 0)

    if Pa_count > Pb_count:
        print('#{} {}'.format(tc + 1, 'B'))
    elif Pa_count < Pb_count:
        print('#{} {}'.format(tc + 1, 'A'))
    else:
        print('#{} {}'.format(tc + 1, 0))
