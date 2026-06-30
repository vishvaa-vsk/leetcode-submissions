# Last updated: 30/06/2026, 12:13:19
1class Solution:
2    def islandPerimeter(self, grid: List[List[int]]) -> int:
3        perimeter = 0
4        for i in range(len(grid)):
5            for j in range(len(grid[0])):
6                if grid[i][j] == 1:
7                    perimeter += 4
8                    if i > 0 and grid[i-1][j] == 1:
9                        perimeter -= 2
10                    if j > 0 and grid[i][j-1] == 1:
11                        perimeter -= 2
12        
13        return perimeter