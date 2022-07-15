#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        avg = 0

        # This has a linear notation of O(n)
        for x in salary:
            if x != min_salary and x != max_salary:
                avg += x

        # Take 2 off the length for min and max.
        return avg / (len(salary)-2)

# @lc code=end
