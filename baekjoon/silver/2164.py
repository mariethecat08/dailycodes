from collections import deque

cards = deque(list(range(1, int(input()) + 1)))
while True:
    if len(cards) == 1:
        break
    cards.popleft()
    cards.rotate(-1)
print(cards[0])
