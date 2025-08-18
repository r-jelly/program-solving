class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[-1]
        elif len(nums) == 2:
            return nums[0] if nums[0]>nums[1] else nums[1]
        else:    
            max_rob = [0] * len(nums)
            max_rob[0] = nums[0]
            max_rob[1] = nums[1]
            max_rob[2] = nums[2] + max_rob[0]
            for i in range(3, len(nums)):
                max_rob[i] = nums[i] + max(max_rob[i-2], max_rob[i-3])
            return max(max_rob)

# Solved 10m12s