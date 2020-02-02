import sys
sys.stdin = open('sw4866.txt', 'r')

def check_pairs(p):
    pair_dict = {']': '[', ')': '(', '}': '{'}
    save = []
    for i in p:
        if i in pair_dict.values():
            save.append(i)
        elif i in pair_dict:
            if len(save) == 0:
                return 0
            elif save[-1] == pair_dict[i]:
                save.pop()
            else:
                return 0
        else:
            continue
    if len(save) == 0:
        return 1
    else:
        return 0


T = int(input())
for tc in range(T):
    result = check_pairs(input())
    print('#%d %d' % (tc+1, result))