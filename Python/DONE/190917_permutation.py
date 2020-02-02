arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(arr)
result = []
for i in range(1 << n):
    temp = []
    for j in range(n+1):
        if i & (1 << j):
            temp.append(arr[j])
    if sum(temp) == 0:
        result.append(temp)
print(result)
