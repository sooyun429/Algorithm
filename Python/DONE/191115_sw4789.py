import sys
sys.stdin = open('sw4789.txt', 'r')

for tc in range(1, int(input())+1):
    info = list(map(int, list(input())))
    res = 0
    for i in range(len(info)):
        # index명 이상일 때 해당 관람객이 박수를 치므로 0이 아닐 때만 고려
        if info[i] != 0:
            # 이전까지의 박수치는 관람객 + 고용한 사람의 수가 index명보다 작은지 확인하고,
            temp = sum(info[:i]) + res
            # 작은 경우 차이만큼 고용인을 더 늘림
            if temp < i:
                res += i-temp
    print('#%d %d' % (tc, res))


