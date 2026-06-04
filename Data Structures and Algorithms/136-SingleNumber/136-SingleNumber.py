# Last updated: 6/4/2026, 6:36:03 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result