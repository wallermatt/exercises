'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


a*b
a*aa* 1+ a

a*. = 1+ a or 1 other char


.* = any
.*a =

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        ast_char = ""
        ast_start = -1
        #import pdb; pdb.set_trace()
        for i, e in enumerate(p):
            if e == "*":
                continue
            if i + 1 < len(p) and p[i + 1] == "*":
                ast_char = e
                ast_start = s_idx
                while s_idx < len(s) and ast_char == s[s_idx]:
                    s_idx += 1
                ast_char = ""
                ast_start = -1
                continue
            if s_idx == len(s):
                return False
            if e == s[s_idx] or e == '.':
                s_idx += 1
            else:
                return False
        if s_idx != len(s):
            return False
        return True


s = Solution()

assert s.isMatch("ac", "a*.") == False
assert s.isMatch("", "a*") == True
assert s.isMatch("a", "a*") == True
assert s.isMatch("aa", "a*") == True
assert s.isMatch("aaaaa", "a*") == True
assert s.isMatch("", "") == True
assert s.isMatch("a", "a") == True
assert s.isMatch("a", ".") == True
assert s.isMatch("ab", "ab") == True
assert s.isMatch("ab", "a.") == True
assert s.isMatch("abc", "a.") == False
assert s.isMatch("ac", "a*.") == False
