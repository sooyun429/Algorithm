import sys
sys.stdin = open('sw4869.txt', 'r')

factobox = [1, 1]
# factobox(n)에서 n과 인덱스 일치시키기 위해 factobox[0]값 입력
# factobox[0]인 경우 result 계산에서 zero division error 없애기 위해 1값을 넣어줌
def factorial(n):
    if n >= len(factobox):
        while len(factobox) <= n:
            factobox.append(len(factobox)*factobox[-1])
    return factobox[n]

T = int(input())
for tc in range(T):
    N = int(input())
    result = 0
    for i in range(N//20+1):  # 길이 20짜리가 들어가는 경우를 하나씩 증가
        twenties_cnt = i
        tens_cnt = N//10 - i*2
        space = twenties_cnt + tens_cnt  # 경우의 수 팩토리얼 활용
        result += (factorial(space)/(factorial(twenties_cnt)*factorial(tens_cnt)))*(2**i)
    print('#%d %d' % (tc+1, result))
