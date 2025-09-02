class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}

        for i in range(m):
            for j in range(n):
                diagonal_sum = i + j
                if diagonal_sum not in diagonals:
                    diagonals[diagonal_sum] = []
                diagonals[diagonal_sum].append(mat[i][j])
        
        for diagonal_sum in sorted(diagonals.keys()):
            if diagonal_sum % 2 == 0:
                result.extend(diagonals[diagonal_sum][::-1])
            else:
                result.extend(diagonals[diagonal_sum])
        
        return result