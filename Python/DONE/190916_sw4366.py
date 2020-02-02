import sys
sys.stdin = open('sw4366.txt', 'r')

def comparison(binary_num, triple_num):
    b_len, t_len = len(binary_num), len(triple_num)
    for i in range(b_len):
        for j in range(2):
            binary_temp = binary_num[:i] + [j] + binary_num[i + 1:]
            b_num = 0
            for k in range(b_len):
                b_num += int(binary_temp[k]) * (2 ** (b_len - k - 1))
            for k in range(t_len):
                for l in range(3):
                    triple_temp = triple_num[:k] + [l] + triple_num[k + 1:]
                    t_num = 0
                    for m in range(t_len):
                        t_num += int(triple_temp[m]) * (3 ** (t_len - m - 1))
                    if b_num == t_num:
                        return b_num

T = int(input())
for tc in range(1, T+1):
    binary = list(input())
    triple = list(input())
    print('#%d %d' % (tc, comparison(binary, triple)))
