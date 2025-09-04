class Solution(object):
    def findClosest(self, x, y, z):
        x_to_z = abs(x - z) # Distance for person 1
        y_to_z = abs(y - z) # Distance for person 2

        if x_to_z < y_to_z:
            return 1 # Person 1 arrives first
        elif x_to_z > y_to_z:
            return 2 # Person 2 arrives first
        else:
            return 0 # Same distance