class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        nums.sort()
        op_cnt = 0
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == k:
                op_cnt += 1
                left += 1
                right -= 1
            elif cur_sum < k:
                left += 1
            elif cur_sum > k:
                right -= 1

        return op_cnt
    
# Solved 5m15s