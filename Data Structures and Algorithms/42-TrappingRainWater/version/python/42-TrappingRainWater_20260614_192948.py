# Last updated: 14/06/2026, 19:29:48
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l,r = 0, len(height)-1
4        leftmax, rightmax = height[l],height[r]
5        water = 0
6
7        while(l < r):
8            if leftmax < rightmax:
9                l += 1
10                leftmax = max(leftmax,height[l])
11                water += leftmax - height[l]
12            else:
13                r -= 1
14                rightmax = max(rightmax,height[r])
15                water += rightmax - height[r]
16        
17        return water
18        