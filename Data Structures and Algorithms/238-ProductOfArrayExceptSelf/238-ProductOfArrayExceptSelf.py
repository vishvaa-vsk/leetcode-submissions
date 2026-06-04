# Last updated: 6/4/2026, 6:35:44 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        ans[0] = 1

        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        rightProd = 1
        for r in range(len(nums)-1,-1,-1):
            ans[r] *= rightProd
            rightProd *= nums[r]

        return ans


        