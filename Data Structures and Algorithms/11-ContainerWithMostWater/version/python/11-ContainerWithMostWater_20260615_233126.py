# Last updated: 15/06/2026, 23:31:26
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        max_area = 0
4        i, j = 0, len(height)-1
5        while (i < j):
6            l = min(height[i],height[j])
7            b = j - i
8            area = l * b
9            max_area = max(area,max_area)
10            if height[i] <= height[j]:
11                i += 1
12            else:
13                j -= 1
14        return max_area