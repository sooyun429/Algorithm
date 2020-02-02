import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
# for i in range(1, T+1):
#     num = list(map(int, input().split()))
#     num1, num2 = num[0], num[1]
#     count = 0
#     pocket1 = input().split()
#     pocket2 = input().split()
#     if num1 > num2:
#         for i in range(num2):
#             if pocket2[i] in pocket1:
#                 count += 1
#     else:
#         for i in range(num1):
#             if pocket1[i] in pocket2:
#                 count += 1
#     print('#%d %d' % (i, count))
#

# T = int(input())
# for i in range(1, T+1):
#     num = list(map(int, input().split()))
#     count = 0
#     pocket1 = input().split()
#     pocket2 = input().split()
#     pocket1.extend(pocket2)
#     pocket1.sort()
#     elements = set(pocket1)
#     for j in elements:
#         if pocket1.count(j) == 2:
#             count += 1
#     print('#%d %d' % (i, count))
#

T = int(input())
for i in range(1, T+1):
    num = list(map(int, input().split()))
    count = 0
    pocket1 = input().split()
    pocket2 = input().split()
    pocket1.extend(pocket2)
    pocket1.sort()
    for j in range(0, len(pocket1)-1):
        if pocket1[j] == pocket1[j+1]:
            count += 1
    print('#%d %d' % (i, count))