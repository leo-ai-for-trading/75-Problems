class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        - from first row, iterate every single nodes from the second row through dfs and to the same with the bottom line and iterate the upper row and use set to avoid duplicate
        """
        ROWS, COLS = len(heights),len(heights[0])
        pac, atl = set(),set()
        
        def dfs(r,c ,visit, prevH):
            #prevH: previous height
            #go from the ocean to the cells
            if ((r,c) in visit or 
               r < 0 or c < 0 or r == ROWS or c == COLS or                    heights[r][c] < prevH):
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r , c+ 1, visit, heights[r][c])
            dfs(r , c - 1, visit, heights[r][c])
                
        for c in range(COLS):
            #first row: pacific ocean
            dfs(0, c, pac, heights[0][c])
            #now the last row
            dfs(ROWS -1 ,c, atl, heights[ROWS - 1][c])
            
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            
        ans = []    
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r,c) in atl:
                    ans.append([r,c])
        return ans
