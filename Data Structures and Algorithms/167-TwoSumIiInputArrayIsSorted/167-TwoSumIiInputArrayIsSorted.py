# Last updated: 6/4/2026, 6:35:56 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            elif currentSum == target:
                return [l+1,r+1]
        return