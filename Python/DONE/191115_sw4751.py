import sys
sys.stdin = open('sw4751.txt', 'r')

for tc in range(1, int(input())+1):
    res = ['.' for _ in range(2)] + ['' for _ in range(3)]
    res[2] = input()
    N = len(res[2])
    res[0] += '.#..'*N
    res[1] += '#.#.'*N
    res[3], res[4] = res[1], res[0]
    temp = '#'
    for letter in res[2]:
        temp += '.'+letter+'.#'
    res[2] = temp
    for line in res:
        print(line)