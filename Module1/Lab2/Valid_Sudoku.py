import sys
board=[]
num=int(input())
for i in range(num):
    board.append(input().split(' '))
def is_valid_sudoku(board):
    # Check rows
    if not check_rows(board):
        return False
    
    # Check columns
    if not check_columns(board):
        return False
    
    # Check sub-boxes
    if not check_sub_boxes(board):
        return False
    
    # All conditions are satisfied
    return True


def check_rows(board):
    for row in board:
        num_set = set()
        for num in row:
            if num != '.':
                if num in num_set:
                    return False
                num_set.add(num)
    return True


def check_columns(board):
    for col in range(9):
        num_set = set()
        for row in range(9):
            num = board[row][col]
            if num != '.':
                if num in num_set:
                    return False
                num_set.add(num)
    return True


def check_sub_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            num_set = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    num = board[row][col]
                    if num != '.':
                        if num in num_set:
                            return False
                        num_set.add(num)
    return True


if is_valid_sudoku(board):
    print("YES")
else:
    print("NO")
                                                                                                                            