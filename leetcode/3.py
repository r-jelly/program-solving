class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        possible_length = len(set(s))
        for i in range(len(s)):
            start_index = max(0, i-possible_length)
            for j in range(start_index, i+1):
                if max_length > (i-j):
                    break
                cur_string = s[j:i+1]
                if len(cur_string) == len(set(cur_string)):
                    if max_length < len(cur_string):
                        max_length = len(cur_string)
                        break

        return max_length
    
# Solved 26m20s