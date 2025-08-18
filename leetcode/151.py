class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        word_list.reverse()
        return " ".join(word_list)

# Solved 1m4s