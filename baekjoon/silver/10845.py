from collections import deque
import sys


def pop(x):
    try:
        return x.popleft()
    except IndexError:
        return -1


def empty(x):
    if len(x) == 0:
        return 1
    else:
        return 0


def front(x):
    if len(x) == 0:
        return -1
    else:
        return x[0]


def back(x):
    if len(x) == 0:
        return -1
    else:
        return x[-1]


n = int(input())
queue = deque()
for i in range(n):
    command = str(sys.stdin.readline())
    if " " in command:
        queue.append(command.split()[1])
    elif command.split()[0] == "pop":
        print(pop(queue))
    elif command.split()[0] == "size":
        print(len(queue))
    elif command.split()[0] == "empty":
        print(empty(queue))
    elif command.split()[0] == "front":
        print(front(queue))
    else:
        print(back(queue))
