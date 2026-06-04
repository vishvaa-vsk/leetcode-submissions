# Last updated: 6/4/2026, 6:35:51 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        result = len(numsSet) < len(nums)
        return result