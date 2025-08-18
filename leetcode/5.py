class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = ""
        for i in range(len(s)+1):
            for j in range(i):
                cur_str = s[j:i]
                if cur_str == cur_str[::-1]:
                    if len(max_str) < len(cur_str):
                        max_str = cur_str

        return max_str
    
# Solved 15m21s