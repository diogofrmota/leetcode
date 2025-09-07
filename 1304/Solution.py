class Solution(object):
    def sumZero(self, n):
        lst = []
        if n % 2 != 0:
            lst.append(0)
        
        for i in range(1, n//2 + 1):
            lst.append(i)
            lst.append(-i)
        
        return lst   