import sys
sys.stdin = open('sw3376_input.txt', 'r')

# P = [0, 1, 1, 1, 2, 2]
#
# def tri(n):
#     if n < 6:
#         return P[n]
#     else:
#         return tri(n - 5) + tri(n - 1)
#
# T = int(input())
#
# for tc in range(T):
#     num = int(input())
#     print('#%d %d' % (tc + 1, tri(num)))
#

T = int(input())
nums = [0] * T
for tc in range(T):
    nums[tc] = int(input())
max_num = max(nums)

P = [0, 1, 1, 1, 2, 2]
if max_num-5:
    P += [0] * (max_num-5)
    for i in range(6, max_num+1):
        P[i] = P[i-5] + P[i-1]
for num in range(len(nums)):
    print('#%d %d' % (num + 1, P[nums[num]]))