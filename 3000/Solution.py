class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        # Initialize variables
        max_diagonal_sq = 0
        max_area = 0

        # Iterate rectangle dimensions
        for rect in dimensions:
            l = rect[0]
            w = rect[1]
            diagonal_sq = l * l + w * w
            area = l * w
            
            if diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = diagonal_sq
                max_area = area

            if diagonal_sq == max_diagonal_sq:
                if area > max_area:
                    max_area = area
        
        return max_area