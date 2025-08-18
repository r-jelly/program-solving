class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_to_right_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            left_to_right_prod[i] = left_to_right_prod[i-1] * nums[i-1]

        right_to_left_prod = nums[-1]
        for i in reversed(range(0, len(nums)-1)):
            left_to_right_prod[i] *= right_to_left_prod
            right_to_left_prod *= nums[i]

        return left_to_right_prod
    
# Solved 19m45s