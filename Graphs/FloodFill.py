from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Performs a flood fill on a 2D image starting at (sr, sc) with the new color.
        """
        # Dimensions of the image
        R, C = len(image), len(image[0])
        
        # Original color of the starting pixel
        curr_color = image[sr][sc]

        # If the starting pixel is already the new color, nothing to do
        if curr_color == newColor:
            return image

        # Recursive helper function to fill connected pixels
        def dfs(r: int, c: int):
            # Only fill pixels that match the original color
            if image[r][c] == curr_color:
                image[r][c] = newColor  # Paint the pixel
                
                # Explore neighbors: up, down, left, right
                if r >= 1:
                    dfs(r - 1, c)  # up
                if r + 1 < R:
                    dfs(r + 1, c)  # down
                if c >= 1:
                    dfs(r, c - 1)  # left
                if c + 1 < C:
                    dfs(r, c + 1)  # right

        # Start DFS from the starting pixel
        dfs(sr, sc)

        return image
