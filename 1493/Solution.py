class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zero_count = 0
        max_lenght = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_lenght = max(max_lenght, right - left)
        
        return max_lenght