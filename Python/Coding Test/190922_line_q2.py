import itertools

nums = list(map(int, input().split()))
perms = list(itertools.permutations(nums))
perms.sort()
k = int(input())
for i in perms[k-1]:
    print(i, end='')
