class Solution(object):
    def flowerGame(self, n, m):
        even_x = n // 2
        odd_x = (n + 1) // 2
        even_y = m // 2
        odd_y = (m + 1) // 2
        return even_x * odd_y + odd_x * even_y