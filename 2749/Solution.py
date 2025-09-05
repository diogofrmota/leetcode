class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        n1 = num1
        n2 = num2
        for k in range(1, 101):
            x = n1 - k * n2
            if x < k:
                continue
            if bin(x).count('1') <= k:
                return k
        return -1