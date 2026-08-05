class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        cols = len(matrix[0])
        h = [0] * (cols + 1)

        for row in matrix:
            for i in range(cols):
                h[i] = h[i] + 1 if row[i] == '1' else 0

            stack = [-1]
            for i, hi in enumerate(h):
                while stack[-1] != -1 and h[stack[-1]] >= hi:
                    curr_hi = h[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, curr_hi * w)
                stack.append(i)
        return max_area        

