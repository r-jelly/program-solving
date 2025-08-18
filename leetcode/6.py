class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = [[""]*len(s) for i in range(numRows)]
        row, col = 0, 0

        for c in s:
            zigzag[row][col] = c
            if numRows == 1:
                col += 1
                continue

            if row == 0:
                row += 1
            elif row == numRows-1:
                row -= 1
                col += 1
            else:
                if col % (numRows-1) == 0:
                    row += 1
                else:
                    row -= 1
                    col += 1
        
        answer_str = ""
        for row_list in zigzag:
            answer_str += "".join(row_list)
        return answer_str 

# Solved 11m41s
# 더 나은 풀이로 해결해보기