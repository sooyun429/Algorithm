import sys
sys.stdin = open('sw3750.txt', 'r')

T = int(input())
result = [0] * T
for tc in range(T):
    nums = list(input())
    while len(nums) > 1:
        temp = 0
        for num in nums:
            temp += int(num)
        nums = list(str(temp))
    result[tc] = '#%d %s' % (tc+1, nums[0])
print('\n'.join(result))
