matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one_position = (i, j)
moves = abs(one_position[0] - 2) + abs(one_position[1] - 2)
print(moves)