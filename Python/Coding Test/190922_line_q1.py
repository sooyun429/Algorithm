a, b = map(int, input().strip().split(' '))
C = [0] * b
Mtime = [int(input()) for _ in range(a)]
idx = time = 0
while idx < a:
    for i in range(len(C)):
        if idx < a and C[i] <= time:
            C[i] += Mtime[idx]
            idx += 1
    time += 1
print(max(C))
