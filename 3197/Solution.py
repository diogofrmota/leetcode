class Solution(object):
    def minimumSum(self, grid):
        m, n = len(grid), len(grid[0])
        
        min_i, max_i = m, -1
        min_j, max_j = n, -1
        ones = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)
                    ones.append((i, j))
        
        if not ones:
            return 0
        
        def get_area(points):
            if not points:
                return 0
            min_r = min(p[0] for p in points)
            max_r = max(p[0] for p in points)
            min_c = min(p[1] for p in points)
            max_c = max(p[1] for p in points)
            return (max_r - min_r + 1) * (max_c - min_c + 1)
        
        min_area = float('inf')

        for split1 in range(min_i, max_i + 1):
            for split2 in range(split1 + 1, max_i + 1):
                rect1 = [(i, j) for i, j in ones if i <= split1]
                rect2 = [(i, j) for i, j in ones if split1 < i <= split2]
                rect3 = [(i, j) for i, j in ones if i > split2]

                if rect1 and rect2 and rect3:
                    area1 = get_area(rect1)
                    area2 = get_area(rect2)
                    area3 = get_area(rect3)
                    min_area = min(min_area, area1 + area2 + area3)
        
        for split1 in range(min_j, max_j + 1):
            for split2 in range(split1 + 1, max_j + 1):
                rect1 = [(i, j) for i, j in ones if j <= split1]
                rect2 = [(i, j) for i, j in ones if split1 < j <= split2]
                rect3 = [(i, j) for i, j in ones if j > split2]

                if rect1 and rect2 and rect3:
                    area1 = get_area(rect1)
                    area2 = get_area(rect2)
                    area3 = get_area(rect3)
                    min_area = min(min_area, area1 + area2 + area3)
        
        # Add the mixed splits part
        for h_split in range(min_i, max_i + 1):
            for v_split in range(min_j, max_j + 1):
                # Case 1: First split horizontally, then vertically on bottom part
                top = [(i, j) for i, j in ones if i <= h_split]
                bottom = [(i, j) for i, j in ones if i > h_split]
                
                if top and bottom:
                    # Split bottom part vertically
                    bottom_left = [(i, j) for i, j in bottom if j <= v_split]
                    bottom_right = [(i, j) for i, j in bottom if j > v_split]
                    
                    if bottom_left and bottom_right:
                        area1 = get_area(top)
                        area2 = get_area(bottom_left)
                        area3 = get_area(bottom_right)
                        min_area = min(min_area, area1 + area2 + area3)
                
                # Case 2: First split horizontally, then vertically on top part
                top_left = [(i, j) for i, j in top if j <= v_split]
                top_right = [(i, j) for i, j in top if j > v_split]
                
                if top_left and top_right:
                    area1 = get_area(top_left)
                    area2 = get_area(top_right)
                    area3 = get_area(bottom)
                    min_area = min(min_area, area1 + area2 + area3)
                
                # Case 3: First split vertically, then horizontally on right part
                left = [(i, j) for i, j in ones if j <= v_split]
                right = [(i, j) for i, j in ones if j > v_split]
                
                if left and right:
                    # Split right part horizontally
                    right_top = [(i, j) for i, j in right if i <= h_split]
                    right_bottom = [(i, j) for i, j in right if i > h_split]
                    
                    if right_top and right_bottom:
                        area1 = get_area(left)
                        area2 = get_area(right_top)
                        area3 = get_area(right_bottom)
                        min_area = min(min_area, area1 + area2 + area3)
                
                # Case 4: First split vertically, then horizontally on left part
                left_top = [(i, j) for i, j in left if i <= h_split]
                left_bottom = [(i, j) for i, j in left if i > h_split]
                
                if left_top and left_bottom:
                    area1 = get_area(left_top)
                    area2 = get_area(left_bottom)
                    area3 = get_area(right)
                    min_area = min(min_area, area1 + area2 + area3)
        
        return min_area