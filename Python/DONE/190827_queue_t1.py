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

Q = [0]*10000
front = rear = -1
enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())

