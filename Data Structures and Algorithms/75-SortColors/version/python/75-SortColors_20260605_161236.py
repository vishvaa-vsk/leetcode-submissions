# Last updated: 6/5/2026, 4:12:36 PM
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
11                temp = nums[low]
12                nums[low] = nums[mid]
13                nums[mid] = temp
14                low += 1
15                mid += 1
16            elif nums[mid] == 1:
17                mid += 1
18            elif nums[mid] == 2:
19                temp = nums[high]
20                nums[high] = nums[mid]
21                nums[mid] = temp
22                high -= 1
23        return
24
25        