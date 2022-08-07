'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        matches = {}
        for i,l in enumerate(s):
            if l in matches:
                matches[l] = matches[l] + [i]
            else:
                matches[l] = [i]
        longest_substring = ""
        for l in matches:
            if len(matches[l]) == 1:
                continue
            for left, right in self.get_pairs(matches[l]):
                ss = s[left:right+1]
                if self.check_palindrome(ss):
                    if len(ss) > len(longest_substring):
                        longest_substring = ss
        return longest_substring

    def get_pairs(self, positions):
        pairs = []
        for i,left in enumerate(positions):
            for right in positions[i+1:]:
                pairs.append([left, right])
        return pairs

    def check_palindrome(self, s):
        len_s = len(s)
        left_s = s[:len_s//2]
        if len_s % 2 == 1:
            right_s = s[(len_s//2)+1:]
        else:
            right_s = s[(len_s//2):]
        if left_s == right_s[::-1]:
            return True
        return False

s = Solution()
assert s.longestPalindrome("babad") == "bab"
assert s.longestPalindrome("cbbd") == "bb"
        