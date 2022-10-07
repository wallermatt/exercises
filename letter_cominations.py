'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

2 = abc
3 = def
4 = ghi
5 = jkl
6 = mno
7 = pqrs
8 = tuv
9 = wxyz


'''
from typing import List


class Solution:

    digits_to_letters = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        elif len(digits) == 1:
            return self.digits_to_letters[digits]
        
        total_combinations = []
        inner_combinations = self.letterCombinations(digits[1:])
        outer_combinations = self.digits_to_letters[digits[0]]
        if inner_combinations == []:
            return outer_combinations
        elif outer_combinations == []:
            return inner_combinations
        for l in outer_combinations:
            for i in inner_combinations:
                total_combinations.append(l + i)
        return total_combinations

s = Solution()

assert s.letterCombinations("2") == ["a", "b", "c"]
assert s.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(s.letterCombinations("1"))
print(s.letterCombinations("12"))
print(s.letterCombinations("234"))
print(s.letterCombinations("12131111114"))