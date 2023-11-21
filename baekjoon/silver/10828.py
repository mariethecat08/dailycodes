import sys


def pop(x):
    try:
        return x.pop()
    except IndexError:
        return -1


def empty(x):
    if len(x) == 0:
        return 1
    else:
        return 0


def top(x):
    try:
        return x[-1]
    except IndexError:
        return -1


n = int(input())
stack = []
for _ in range(n):
    command = str(sys.stdin.readline())
    if " " in command:
        stack.append(command.split()[1])
    elif command.split()[0] == "pop":
        print(pop(stack))
    elif command.split()[0] == "size":
        print(len(stack))
    elif command.split()[0] == "empty":
        print(empty(stack))
    else:
        print(top(stack))
