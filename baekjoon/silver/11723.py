import sys


def remove(sets, x):
    try:
        sets.remove(x)
        return sets
    except KeyError:
        return sets


n = int(input())
S = set()
for _ in range(n):
    command = sys.stdin.readline()
    if command.split()[0] == "add":
        S.add(command.split()[1])
    elif command.split()[0] == "remove":
        remove(S, command.split()[1])
    elif command.split()[0] == "check":
        if command.split()[1] in S:
            print(1)
        else:
            print(0)
    elif command.split()[0] == "toggle":
        if command.split()[1] in S:
            remove(S, command.split()[1])
        else:
            S.add(command.split()[1])
    elif command.split()[0] == "all":
        S = set(map(str, range(1, 21)))
    else:
        S = set([])
