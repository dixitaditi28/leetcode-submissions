
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])

        rtrack = [0] * r
        ctrack = [0] * c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rtrack[i] = -1
                    ctrack[j] = -1

        for i in range(r):
            for j in range(c):
                if rtrack[i] == -1 or ctrack[j] == -1:
                    matrix[i][j] = 0