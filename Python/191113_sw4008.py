import sys, itertools
sys.stdin = open('sw4008.txt', 'r')

def perm(temp, oper_arr, idx):
    global numbers, N, minnum, maxnum
    for j in range(len(oper_arr)):
        oper = oper_arr[j]
        if oper == '+':
            temp += numbers[idx]
        elif oper == '-':
            temp -= numbers[idx]
        elif oper == '*':
            temp *= numbers[idx]
        else:
            temp //= numbers[idx]
        if len(oper_arr) == 1:
            if temp < minnum: minnum = temp
            if temp > maxnum: maxnum = temp
            break
        perm(temp, oper_arr[:j] + oper_arr[j + 1:], idx + 1)

for tc in range(1, int(input())+1):
    N = int(input())
    oper_num = list(map(int, input().split()))
    opers = ['+', '-', '*', '/']
    for i in range(4):
        opers += [opers[i] for _ in range(oper_num[i])]
    opers = opers[4:]
    numbers = list(map(int, input().split()))
    minnum, maxnum = 100000000, -100000000
    perm(numbers[0], opers, 1)
    print('#%d %d' % (tc, abs(maxnum-minnum)))

# ## itertools를 쓰면 메모리 초과하고 시간초과남
# for tc in range(1, int(input())+1):
#     N = int(input())
#     oper_num = list(map(int, input().split()))
#     opers = ['+', '-', '*', '/']
#     for i in range(4):
#         opers += [opers[i] for _ in range(oper_num[i])]
#     opers = opers[4:]
#     numbers = list(map(int, input().split()))
#     min, max = 100000000, -100000000
#     for p in itertools.permutations(range(N-1)):
#         temp = numbers[0]
#         for i in range(1, N):
#             oper = opers[p[i-1]]
#             if oper == '+':
#                 temp += numbers[i]
#             elif oper == '-':
#                 temp -= numbers[i]
#             elif oper == '*':
#                 temp *= numbers[i]
#             else:
#                 temp //= numbers[i]
#         if temp < min: min = temp
#         if temp > max: max = temp
#     print('#%d %d' % (tc, abs(max-min)))
