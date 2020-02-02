import sys
sys.stdin = open('sw1244.txt', 'r')

def change(array):
    maxnumber = max(array)
    idx = []
    for i in range(len(array)):
        if array[i] == maxnumber:
            idx.append(i)


T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())
    N = list(map(int, list(a)))
    turn = int(b)
    N_length = len(N)
    maxnum = [i for i in N]  # 주어진 숫자로 만들 수 있는 최대값 만들기
    maxnum.sort(reverse=True)
    s = 0
    for i in range(N_length):
        if maxnum[i] != N[i]:
            s = i
            break
    while turn:
        exchange = 1

                for k in range(N_length-1, -1, -1):
                    if N[k] == maxnum[j]:
                        N[j], N[k] = N[k], N[j]
                        exchange = 0
                        break
                if exchange == 0:
                    break
        if exchange:
            for j in range(len(N)-1):
                if N[j] == N[j+1]:
                    N[j], N[j+1] = N[j+1], N[j]
                    exchange = 0
                    break
            if exchange:
                N[-2], N[-1] = N[-1], N[-2]
    result = ''.join([str(i) for i in N])
    print('#%d %s' % (tc, result))


