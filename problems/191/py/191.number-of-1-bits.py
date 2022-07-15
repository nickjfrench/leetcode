#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        count = 0

        for c in bin_n:
            if c == '1':
                count += 1

        return count
# @lc code=end
