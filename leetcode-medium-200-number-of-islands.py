class Solution:
    def is_valid(self, i, j):
        return i >= 0 and i < self.m and j >= 0 and j < self.n
    
    def search(self, i, j):
        self.grid[i][j] = '0'
        
        self.explore(i, j-1)
        self.explore(i, j+1)
        self.explore(i-1, j)
        self.explore(i+1, j)

    def explore(self, i, j):
        if self.is_valid(i, j) and self.grid[i][j] == '1':
            self.search(i, j)
            return True
        return False

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        
        islands = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.explore(i, j):
                    islands += 1
        return islands
