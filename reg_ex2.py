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

a*. = b,a,aa,aab = 0+ a & ., 1+ a,

a*b* = 0+ a & 0+ b

a*a* = 0+ a

a*.b* = 0+ a & . & 0+ b, 1+a & 0+ b, 0+ a & 1+ b

a*a = 1+ a


aaaa



'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        s_idx = 0
        p_idx = 0
        while p_idx < p_len:
            exp = p[p_idx]
            if p



s = Solution()

assert s.isMatch("a", "a*.") == True
assert s.isMatch("c", "a*.") == True
assert s.isMatch("aac", "a*.") == True
assert s.isMatch("ac", "a*.") == True
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
