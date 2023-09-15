# n = int(input())
# words = set([input() for _ in range(n)])

# words = sorted(list(words))
# words = sorted(words, key=lambda x: len(x))
# for i in range(len(words)):
#     print(words[i])

n = int(input())
words = set([input() for _ in range(n)])


words = sorted(words, key=lambda x: len(x))
words = sorted(list(words))
for i in range(len(words)):
    print(words[i])
