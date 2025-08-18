class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        hash1, hash2 = dict(), dict()

        for i in range(len(word1)):
            if word1[i] in hash1:
                hash1[word1[i]] += 1
            else:
                hash1[word1[i]] = 1

        for i in range(len(word2)):
            if word2[i] in hash2:
                hash2[word2[i]] += 1
            else:
                hash2[word2[i]] = 1

        key1 = sorted(list(hash1))
        key2 = sorted(list(hash2))

        value1 = sorted(list(hash1.values()))
        value2 = sorted(list(hash2.values()))

        if key1 == key2 and value1 == value2:
            return True
        else:
            return False
        
# Solved 13m57s
# Memory를 더 적게 쓰는 방법??