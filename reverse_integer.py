'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10:
            return x
        reversed_x = 0
        if x >= 0:
            multiplier = 1
        else:
            multiplier = -1 
        while abs(x) >= 10:
            d = x % (10 * multiplier)
            reversed_x *= 10
            reversed_x += d 
            x = (abs(x) // 10) * multiplier
        reversed_x *= 10
        reversed_x += x
        if reversed_x > 2**31 - 1:
            return 0
        elif reversed_x < -2**31:
            return 0
        return reversed_x


s = Solution()

assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(12) == 21
