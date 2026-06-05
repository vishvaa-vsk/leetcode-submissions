# Last updated: 6/5/2026, 4:14:07 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        low, mid = 0, 0
7        high = len(nums) - 1
8
9        while mid <= high:
10            if nums[mid] == 0:
11                nums[low], nums[mid] = nums[mid], nums[low]
12                low += 1
13                mid += 1
14            elif nums[mid] == 1:
15                mid += 1
16            elif nums[mid] == 2:
17                nums[high], nums[mid] = nums[mid], nums[high]
18                high -= 1
19        return
20
21        