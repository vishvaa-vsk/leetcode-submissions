# Last updated: 6/7/2026, 11:25:17 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        max_area = 0
4        l,r = 0, len(height)-1
5
6        while (l<r):
7            h = min(height[l],height[r])
8            w = r - l
9            area = h * w
10            max_area = max(max_area,area)
11            if height[l] <= height[r]:
12                l += 1
13            else:
14                r -= 1
15        return max_area
16
17        