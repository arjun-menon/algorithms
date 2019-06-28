class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        
        boundaries = []
        offset_i = 0
        offset_j = 0
        while True:
            # 1
            for j in range(offset_j, n - offset_j):
                boundaries.append(matrix[offset_i][j])
            # 2
            if (offset_i + 1) < (m - offset_i - 1):
                for i in range(offset_i + 1, m - offset_i - 1):
                    boundaries.append(matrix[i][n - offset_j - 1])
            # 3
            if (m - offset_i - 1) > offset_i:
                for j in reversed(range(offset_j, n - offset_j)):
                    boundaries.append(matrix[m - offset_i - 1][j])
            # 4
            if (offset_i + 1) < (m - offset_i - 1)  and (offset_j + 1) < (n - offset_j):
                for i in reversed(range(offset_i + 1, m - offset_i - 1)):
                    boundaries.append(matrix[i][offset_j])
            
            offset_i += 1
            offset_j += 1
            
            if offset_i >= (m - 1) or offset_j >= (n - 1):
                break

        return boundaries
