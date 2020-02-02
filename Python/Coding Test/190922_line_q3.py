N = int(input())
times = [[0, 0] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    times[i][1], times[i][0] = a, b
times.sort()
idx = 0
toilet = [0]*N
while idx < N:
    for i in range(len(toilet)):
        if times[idx][1] >= toilet[i]:
            toilet[i] = times[idx][0]
            idx += 1
            break
cnt = 0
for i in toilet:
    if i:
        cnt += 1
print(cnt)
