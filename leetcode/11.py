class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        max_size = 0
        while left < right:
            cur_size = min(height[left], height[right]) * (right-left)
            if cur_size > max_size:
                max_size = cur_size
            
            if height[left] < height[right]:
                left += 1
            else: right -= 1
        return max_size
    
# Solved 3m17s