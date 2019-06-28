class Solution:
    def numIslands(self, grid): # :type grid: List[List[str]] :rtype: int
        def search(i, j):
            if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                search(i, j-1)
                search(i, j+1)
                search(i-1, j)
                search(i+1, j)
                return True
        islands, m, n = 0, len(grid), len(grid[0]) if len(grid) else 0
        for i in range(m):
            for j in range(n):
                if search(i, j):
                    islands += 1
        return islands
