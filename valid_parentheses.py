'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
from queue import LifoQueue


class Solution:
    def isValid(self, s: str) -> bool:
        q = LifoQueue()
        for c in s:
            if c in ["(", "[", "{"]:
                q.put(c)
            else:
                if q.empty():
                    return False
                open_p = q.get()
                if c == ")":
                    if open_p != "(":
                        return False
                elif c == "]":
                    if open_p != "[":
                        return False
                elif c == "}":
                    if open_p != "{":
                        return False
        if q.empty():
            return True
        return False


s = Solution()



assert s.isValid("([)]") == False

assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
