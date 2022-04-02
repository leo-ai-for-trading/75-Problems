class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        - DP
        - dfs
        - cache[r][c]
        - res = sum(right + down)
        - to get bottom row: sum the right cell with down 
        - first column will be 1
        - we start on the bottom row and fill them with 1
        - 
        """
        #bottom row
        row = [1] * n
        for i in range(m - 1):
            newrow = [1] * n #above row
            for j in range(n - 2, -1,-1):
                newrow[j] = newrow[j + 1] + row[j]
            row = newrow
        return row[0]
