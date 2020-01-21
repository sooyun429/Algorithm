import sys
sys.stdin = open('bj1139.txt', 'r')

N = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)
result = 0
for num in range(len(times)):
    result += (num+1)*times[num]
print(result)
