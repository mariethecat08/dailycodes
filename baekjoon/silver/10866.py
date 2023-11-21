import sys
from collections import deque


def popfront(x):
    try:
        return x.popleft()
    except IndexError:
        return -1


def popback(x):
    try:
        return x.pop()
    except IndexError:
        return -1


def empty(x):
    if len(x) == 0:
        return 1
    else:
        return 0


def front(x):
    try:
        return x[0]
    except IndexError:
        return -1


def back(x):
    try:
        return x[-1]
    except IndexError:
        return -1


n = int(input())
deque = deque()
for _ in range(n):
    command = sys.stdin.readline()
    if command.split()[0] == "push_front":
        deque.appendleft(command.split()[1])
    elif command.split()[0] == "push_back":
        deque.append(command.split()[1])
    elif command.split()[0] == "pop_front":
        print(popfront(deque))
    elif command.split()[0] == "pop_back":
        print(popback(deque))
    elif command.split()[0] == "size":
        print(len(deque))
    elif command.split()[0] == "empty":
        print(empty(deque))
    elif command.split()[0] == "front":
        print(front(deque))
    else:
        print(back(deque))
