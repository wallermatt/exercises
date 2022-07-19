'''
Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        starts = {}
        biggest_start = 0
        longest_length = 0
        start_of_seq = 0
        for i, e in enumerate(s):
            if e not in starts:
                starts[e] = i
            else:
                if starts[e] >= biggest_start:
                    biggest_start = starts[e]
                    length = i - start_of_seq
                    if length > longest_length:
                        longest_length = length
                if start_of_seq <= starts[e]:
                    start_of_seq = i
                elif start_of_seq > biggest_start:
                    start_of_seq = starts[e] + 1
                starts[e] = i

        for e in starts:
            if starts[e] > biggest_start or biggest_start == 0:
                length = i - starts[e] + 1
                if length > longest_length:
                    longest_length = length
        return longest_length 

s = Solution()

assert s.lengthOfLongestSubstring("aabaab!bb") == 3

assert s.lengthOfLongestSubstring(" ") == 1
assert s.lengthOfLongestSubstring("cdd") == 2
assert s.lengthOfLongestSubstring("ohomm") == 3
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring("pwwkewxy") == 5
