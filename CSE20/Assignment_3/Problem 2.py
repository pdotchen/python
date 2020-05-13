m, n = input().split()
m = int(m)
n = int(n)
b = int(input())

b_location = []

for i in range(b):
    num = input()
    b_location.append(num)

board = []
for l in range(m):
    row = ['.'] * n
    board.append(row)

for l in b_location:
    x, y = l.split()
    x = int(x)
    y = int(y)
    board[x][y] = '*'

print(board)
for l in range(m):
    for o in range(n):
        around = 0
        if board[l][o] == ".":
            if l + 1 != m and board[l + 1][o] == "*":
                around += 1
            if l + 1 != m and o - 1 >= 0 and board[l + 1][o - 1] == "*":
                around += 1
            if o - 1 >= 0 and board[l][o - 1] == "*":
                around += 1
            if l - 1 >= 0 and o - 1 >= 0 and board[l - 1][o - 1] == "*":
                around += 1
            if l - 1 >= 0 and board[l - 1][o] == "*":
                around += 1
            if l - 1 >= 0 and o + 1 != n and board[l - 1][o + 1] == "*":
                around += 1
            if o + 1 != n and board[l][o + 1] == "*":
                around += 1
            if l + 1 != m and o + 1 != n and board[l + 1][o + 1] == "*":
                around += 1
            board[l][o] = str(around)

for l in board:
    print(" ".join(l))





























