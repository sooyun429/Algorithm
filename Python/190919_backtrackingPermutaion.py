arr = [i for i in range(1, 11)]

n = len(arr)
result = []
for i in range(1<<n):
    temp = []
    for j in range(n+1):
        if i & (1<<j):
            temp.append(arr[j])
    if sum(temp) == 10:
        result.append(temp)
print(result)