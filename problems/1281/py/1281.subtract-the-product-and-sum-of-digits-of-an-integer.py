#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        prod = 1
        sum = 0

        for i in str_n:
            int_i = int(i)
            prod *= int_i
            sum += int_i

        return prod - sum
# @lc code=end
