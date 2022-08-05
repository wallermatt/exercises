'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for e in range(numRows)]
        curr_row = 0
        down = True
        for l in s:
            rows[curr_row] += l
            if down and curr_row < numRows - 1:
                curr_row += 1
            elif down and curr_row == numRows - 1:
                down = False
                curr_row -= 1
            elif not down and curr_row > 0:
                curr_row -= 1
            else:
                down = True
                curr_row += 1
        return "".join(rows)


s = Solution()

assert s.convert("A", 1) == "A"
assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
