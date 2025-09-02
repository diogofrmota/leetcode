class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid) # number of arrays
        diagonals =  {} # initialize

        # Group elements by diagonal d = i - j
        for i in range(n): # row
            for j in range(n): # column
                d = i - j # diagonal index
                if d not in diagonals: # check if diagonal has been seen before
                    diagonals[d] = [] # create an empty list for this diagonal
                diagonals[d].append(grid[i][j]) # add element to the diagonal

        # Sort each diagonal
        for d in diagonals:
            if d >= 0:
                diagonals[d].sort(reverse=True) # Non-increasing for bottom-left
            else:
                diagonals[d].sort() # Increasing for bottom-left
        
        # Reconstruct matrix using sorted diagonals
        result = [[0] * n for _ in range(n)]
        for d, arr in diagonals.items():
            idx = 0
            # Calculate valid i range for this diagonal
            start_i = max(0, d)
            end_i = min(n, n + d)
            for i in range(start_i, end_i):
                j = i - d
                result[i][j] = arr[idx]
                idx += 1

        return result