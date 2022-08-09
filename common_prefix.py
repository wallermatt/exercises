'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        for s in strs:
            if not s:
                return ""
        first_letter = strs[0][0]
        for s in strs[1:]:
            if s[0] != first_letter:
                return ""
        new_strs = [e[1:] for e in strs]
        return first_letter + self.longestCommonPrefix(new_strs)


s = Solution()



assert s.longestCommonPrefix(["cir","car"]) == "c"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
