# Last updated: 6/4/2026, 6:35:35 PM
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.index = {}

        for i in range(self.n):
            for j in range(self.n):
                self.index[self.grid[i][j]] = [i,j]

    def getValue(self,i,j):
        if i < 0 or i >= self.n: return 0
        if j < 0 or j >= self.n: return 0
        return self.grid[i][j]
        
    def adjacentSum(self, value: int) -> int:
        total = 0
        i, j = self.index[value]
        for ni,nj in zip([i-1,i,i+1,i],[j,j-1,j,j+1]):
            total += self.getValue(ni,nj)
        return total

    def diagonalSum(self, value: int) -> int:
        total = 0
        i, j = self.index[value]
        for ni,nj in zip([i-1,i-1,i+1,i+1],[j-1,j+1,j-1,j+1]):
            total += self.getValue(ni,nj)
        return total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)