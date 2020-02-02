import sys
sys.stdin = open('sw5356.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    letters = [list(input()) for _ in range(5)]
    # for l in letters:
    #     print(l, end='\n')
    # print('##############')
    max_len = len(letters[0])
    for l in letters[1:]:
        if len(l) > max_len:
            max_len = len(l)
    result = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(letters[j]):
               result += letters[j][i]
    print('#%d %s' % (tc, result))
