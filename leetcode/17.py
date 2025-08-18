
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        map_digit = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        answer_list = []
        stack = [l for l in map_digit[digits[0]]]
        while stack:
            cur_letter = stack.pop(0)
            if len(cur_letter) == len(digits):
                answer_list.append(cur_letter)
            else:
                for letter in map_digit[digits[len(cur_letter)]]:
                    stack.append(cur_letter + letter)

        return answer_list
    
# Solved 12m34s