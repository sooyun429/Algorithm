import sys, itertools
sys.stdin = open('sw1952.txt', 'r')


def three_months(arr):
    if len(arr) >
    for i in arr[:-2]:


T = int(input())
for tc in range(1, T+1):
    payment = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    for i in range(12):  # 월마다 1일기준요금 vs 한달요금으로 비교해서 값 채워넣기
        if plan[i]:
            plan[i] *= payment[0]
            if plan[i] > payment[1]:
                plan[i] = payment[1]
    print(plan)

    subset = []

    for i in range(1, 4):
        A = [1]*(12-(i*3))
        B = [3]*i
        subset.append(list(itertools.permutations(A+B)))
    print(subset)


    idx = 0
    while idx < 10:
        if months[idx]:
            temp = [months[idx]+plan[idx+3]+plan[idx+4], months[idx+1]+plan[idx]+plan[idx+4], months[idx+2]+plan[idx]+plan[idx+1]]
            mintemp = temp.index(min(temp))
            plan[idx+mintemp], plan[idx+mintemp+1], plan[idx+mintemp+2] = months[idx+mintemp], 0, 0
            print(plan)
            idx += 5
        else:
            idx += 1
    result = sum(plan)
    if result > payment[3]:
        result = payment[3]
    print('#%d %d' % (tc, result))
