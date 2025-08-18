class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        count_str = ''
        string_stack = []
        final_str = []
        for c in s:
            if c.isdigit():
                count_str += c
            else:
                if c == ']':
                    sub_c = string_stack.pop()
                    sub_str = []
                    while sub_c != '[':
                        sub_str.append(sub_c)
                        sub_c = string_stack.pop()
                    sub_str = sub_str[::-1]
                    string_stack.append(''.join(sub_str) * int(count_stack.pop()))
                else:
                    if c == '[':
                        count_stack.append(count_str)
                        count_str = ''
                    string_stack.append(c)
            
        return ''.join(string_stack)
    
# Solved 16m45s