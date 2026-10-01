class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in matrix:
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
                    
            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    max_area = max(max_area, height * (i - idx))
                    start = idx
                stack.append((start, h))
                
        return max_area
        