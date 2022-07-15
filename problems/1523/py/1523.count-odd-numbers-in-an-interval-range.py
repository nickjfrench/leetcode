#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # This method exceeds the time limit for large numbers. This is due to it being O(n).
        # count: int = 0
        # # For Loop needs to be inclusive of the parameters
        # for x in range(low, high+1):
        #     if x % 2 != 0:
        #         count += 1
        # return count

        # The following works and is very efficent as it uses arithmetic progressions. This problem now uses O(1).
        if(low % 2 == 0):
            low += 1
        if(high % 2 == 0):
            high -= 1
        # Double Slash is used for integer division. It will only return the integer, not the floating point.
        return (high-low + 2)//2
# @lc code=end
