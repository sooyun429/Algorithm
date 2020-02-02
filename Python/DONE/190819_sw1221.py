import sys
sys.stdin = open('sw1221_input.txt', 'r')

T = int(input())
for tc in range(T):
    n = input()
    num_dict = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    numbers = list(map(str, input().split()))
    for number in numbers:
        count[number] += 1

    result = ''
    for num in num_dict:
        result += (num + ' ') * count[num]
    print('#%d' % (tc + 1))
    print(result[:-1])