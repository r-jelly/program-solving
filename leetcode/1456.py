class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        check_vowel = [0] * len(s)
        for i, char in enumerate(s):
            if char in ['a', 'e', 'i', 'o', 'u']:
                check_vowel[i] = 1
        
        max_vowel = sum(check_vowel[0:k])
        cur_vowel = max_vowel
        for i in range(1, len(s)-k+1):
            cur_vowel += check_vowel[i+k-1] - check_vowel[i-1]
            max_vowel = max(max_vowel, cur_vowel)
        return max_vowel

# Solved 15m32s
# Python에서의 sum() 함수는 O(n) -> Two pointer를 써서 시간복잡도 줄이기!