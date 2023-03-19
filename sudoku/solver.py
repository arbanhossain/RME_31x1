sudoku = [
    [0, 5, 0, 1, 0, 8, 9, 0, 0],
    [0, 0, 0, 0, 7, 6, 0, 2, 1],
    [7, 0, 0, 3, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 3, 9, 0, 0, 0, 0, 5, 0],
    [0, 1, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 9, 0, 0, 7],
    [0, 0, 0, 2, 0, 3, 0, 0, 0],
    [0, 0, 0, 4, 0, 7, 0, 0, 0]
]


def print_sudoku(s):
    for i in range(len(s)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(s[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(s[i][j], end=" ")
        print()

print_sudoku(sudoku)

def find_first_empty(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(s, num, pos):
    # Check row
    for i in range(len(s[0])):
        if s[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(s)):
        if s[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if s[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(s):
    empty_pos = find_first_empty(s)
    if not empty_pos:
        print_sudoku(s)
        return True
    else:
        row, col = empty_pos
        for i in range(1,10):
            if is_valid(s, i, (row, col)):
                s[row][col] = i
                if solve(s):
                    return True
                s[row][col] = 0
        return False

print()
print("SOLUTION: \n")
solve(sudoku)