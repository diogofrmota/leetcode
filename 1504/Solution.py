class Solution(object):
    def numSubmat(self, mat):
        if not mat or not mat[0]:
            return 0
        
        m,n = len(mat), len(mat[0])
        result = 0

        height = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    height[i][j] = height[i-1][j] + 1 if i > 0 else 1
                else:
                    height[i][j] = 0
        
        for i in range(m):
            stack = []

            for j in range(n):
                while stack and height[i][stack[-1][0]] > height[i][j]:
                    stack.pop()
                
                if not stack:
                    count = height[i][j] * (j + 1)
                else:
                    prev = stack[-1][0]
                    count = height[i][j] * (j - prev) + stack[-1][1]

                result += count
                stack.append((j, count))

        return result