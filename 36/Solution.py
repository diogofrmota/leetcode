class Solution(object):
    def isValidSudoku(self, board):
        # Check each row
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        
        # Check each column
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)

        # Check the 3x3 sub-boxes
        for box_row in range(0, 9, 3):  # 0, 3, 6
            for box_col in range(0, 9, 3):  # 0, 3, 6
                seen = set()
                # Check each cell in the 3x3 box
                for i in range(3):
                    for j in range(3):
                        row = box_row + i
                        col = box_col + j
                        cell = board[row][col]
                        if cell != '.':
                            if cell in seen:
                                return False
                            seen.add(cell)
        
        return True