# 1018 #11.13,16
def count_wrong_color(x: list) -> int:
    color = ["W", "B"]
    small = 10000
    for c in range(2):
        first = color[c]
        second = color[color.index(first) - 1]
        cnt = 0
        for i in range(8):
            for j in range(0, 8, 2):
                if i % 2 == 0 and x[i][j] != first:
                    cnt += 1
                elif i % 2 == 1 and x[i][j] == first:
                    cnt += 1
            for j in range(1, 8, 2):
                if i % 2 == 0 and x[i][j] != second:
                    cnt += 1
                elif i % 2 == 1 and x[i][j] == second:
                    cnt += 1
        if cnt < small:
            small = cnt
    return small


N, M = map(int, input().split())
boards = [list(input()) for _ in range(N)]
minimum = 10000
for i in range(7, N):
    tmp = boards[i - 7: i + 1]
    for j in range(7, M):
        # tmp_board = tmp[:, j - 7 : j + 1]
        tmp_board = [k[j - 7: j + 1] for k in tmp]
        cnt = count_wrong_color(tmp_board)
        if minimum > cnt:
            minimum = cnt
print(minimum)
