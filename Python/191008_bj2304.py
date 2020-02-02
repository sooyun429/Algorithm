import sys
sys.stdin = open('bj2304.txt', 'r')

N = int(input())
pillars = [0]*1000
result = 0
for i in range(N):
    a, b = map(int, input().split())
    pillars[a] = b
for i in range(1000):
    if pillars[i]:
        idx = i
        break
while True:
    if max(pillars[idx+1:]) > pillars[idx]:
        for i in range(idx+1, 1000):
            if pillars[i] > pillars[idx]:
                result += (i-idx)*pillars[idx]
                idx = i
                break
    else:
        if max(pillars[idx+1:]) == pillars[idx]:
            for i in range(idx+1, 1000):
                if pillars[i] == pillars[idx]:
                    result += (i-idx+1)*pillars[idx]
                    idx = i+1
                    break
        else:
            result += pillars[idx]
            idx += 1
            pillars[idx] = max(pillars[idx+1:])
    # print(idx, result)
    if sum(pillars[idx+1:]) == 0:
        break
print(result)
