from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid (r,c):
            return 0<=r<m and 0 <=c < n
            
        m = len(mat)
        n = len(mat[0])
        seen = set ()
        matrix = [ row[:] for row in mat]
        queue = deque()

        for row in range (m):
            for col in range (n):
                if matrix[row][col] == 0:
                    queue.append((row,col,0))
                    seen.add((row,col))
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            cell = queue.popleft()
            i, j, steps = cell

            for dx, dy in directions:
                next_row, next_col = i+dx, j+dy
                if (next_row,next_col) not in seen and valid(next_row, next_col):
                    queue.append((next_row,next_col,steps+1))
                    seen.add((next_row,next_col))
                    matrix[next_row][next_col] = steps + 1
        
        return matrix        
