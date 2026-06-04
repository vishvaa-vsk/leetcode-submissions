# Last updated: 6/5/2026, 12:01:01 AM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        result = []
4        nums.sort()
5        n = len(nums)
6
7        for i in range(n-2):
8            if i>0 and nums[i] == nums[i-1]:
9                continue
10            l,r = i+1, n-1
11
12            while (l < r):
13                s = nums[i] + nums[l] + nums[r]
14                if s == 0:
15                    result.append([nums[i],nums[l],nums[r]])
16                    while l < r and nums[l] == nums[l+1]:
17                        l+=1
18                    while l < r and nums[r] == nums[r-1]:
19                        r-=1
20                    l+=1
21                    r-=1
22                elif s < 0:
23                    l+=1
24                else:
25                    r -= 1
26
27        return result
28
29                
30
31        
32