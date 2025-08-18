class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt_zero = 0
        max_size = 0
        left = 0
        for right in range(len(nums)):
            cnt_zero += 1-nums[right]

            if cnt_zero <= k:
                max_size = max(max_size, right-left+1)
            else:
                left += 1
                cnt_zero -= (1-nums[left-1])

        return max_size
    
# Solved 24m10s 