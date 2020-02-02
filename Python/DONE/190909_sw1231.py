import sys
sys.stdin = open('sw1231.txt', 'r')

def inorder(n):
    global result
    if tree[n][1]:
        inorder(tree[n][1])
    result += tree[n][0]
    if tree[n][2]:
        inorder(tree[n][2])


for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]
    result = ''
    for i in range(N):
        temp = list(map(str, input().split()))
        tree[int(temp[0])][0] = temp[1]
        if len(temp) > 2:
            tree[int(temp[0])][1] = int(temp[2])
        if len(temp) > 3:
            tree[int(temp[0])][2] = int(temp[3])
    inorder(1)
    print('#%d %s' % (tc, result))
