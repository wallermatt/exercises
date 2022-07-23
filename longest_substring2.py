'''
Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        letters_encountered = {}
        longest_length = 0
        start_of_seq = 0
        for i,e in enumerate(s):
            if e not in letters_encountered:
                letters_encountered[e] = i
            else:
                if start_of_seq > letters_encountered[e]:
                    letters_encountered[e] = i
                else:
                    if i - start_of_seq > longest_length:
                        longest_length = i - start_of_seq
                    start_of_seq = letters_encountered[e] + 1
                    letters_encountered[e] = i
            #print(i, e, longest_length, start_of_seq, letters_encountered)
        if i + 1 - start_of_seq > longest_length:
            longest_length = i + 1- start_of_seq

        return longest_length
                


s = Solution()

assert s.lengthOfLongestSubstring("abcabcbb") == 3

assert s.lengthOfLongestSubstring("aabaab!bb") == 3

assert s.lengthOfLongestSubstring(" ") == 1
assert s.lengthOfLongestSubstring("cdd") == 2
assert s.lengthOfLongestSubstring("ohomm") == 3
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring("pwwkewxy") == 5
