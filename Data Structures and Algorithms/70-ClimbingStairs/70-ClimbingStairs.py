# Last updated: 6/4/2026, 6:36:12 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
