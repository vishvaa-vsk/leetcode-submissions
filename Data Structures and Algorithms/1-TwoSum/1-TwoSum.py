# Last updated: 6/4/2026, 6:38:24 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[n] = i
        return