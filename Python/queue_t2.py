def isEmpty():
    return front == rear


def isFull():
    return rear == len(Q) -1


def enQueue(item):
    global rear
    if isFull(): return -1
    else:
        rear += 1
        Q[rear] = item


def deQueue():
    global front
    if isEmpty():
        return -1
    else:
        front += 1
        return Q[front]


def Qpeek():
    if isEmpty():
        return -1
    else:
        return Q[front+1]


Q = [0] * 20
front = rear = -1
snack = [0] * 20
order_number = [1, 1]
cnt = 0
while snack[19] == 0:
    enQueue(order_number)
    print(Q, front, rear)
    turn = Qpeek()
    print(turn)
    for i in range(1, turn[1] + 1):
        snack[cnt] = turn[0]
        cnt += 1
        if cnt == 20:
            break
    deQueue()
    print(Q, front, rear)
    turn[1] += 1
    enQueue(turn)
    print(Q)
    order_number[0] += 1
    print(Q, snack)

print(snack[19])
