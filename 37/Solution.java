public class Solution {
    public void solveSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][10];
        boolean[][] cols = new boolean[9][10];
        boolean[][] boxes = new boolean[9][10];
        
        // Initialize the arrays with existing numbers
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '0';
                    rows[i][num] = true;
                    cols[j][num] = true;
                    int boxIndex = (i / 3) * 3 + j / 3;
                    boxes[boxIndex][num] = true;
                }
            }
        }
        solve(board, rows, cols, boxes, 0, 0);
    }
    
    private boolean solve(char[][] board, boolean[][] rows, boolean[][] cols, boolean[][] boxes, int i, int j) {
        if (i == 9) {
            return true; // reached the end
        }
        int nextI = i, nextJ = j + 1;
        if (nextJ == 9) {
            nextI = i + 1;
            nextJ = 0;
        }
        if (board[i][j] != '.') {
            return solve(board, rows, cols, boxes, nextI, nextJ);
        } else {
            int boxIndex = (i / 3) * 3 + j / 3;
            for (int num = 1; num <= 9; num++) {
                if (!rows[i][num] && !cols[j][num] && !boxes[boxIndex][num]) {
                    board[i][j] = (char) (num + '0');
                    rows[i][num] = true;
                    cols[j][num] = true;
                    boxes[boxIndex][num] = true;
                    if (solve(board, rows, cols, boxes, nextI, nextJ)) {
                        return true;
                    }
                    // backtrack
                    board[i][j] = '.';
                    rows[i][num] = false;
                    cols[j][num] = false;
                    boxes[boxIndex][num] = false;
                }
            }
            return false;
        }
    }
}