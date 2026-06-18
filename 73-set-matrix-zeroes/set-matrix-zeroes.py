class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
     
        r=len(matrix)
        c=len(matrix[0])

        rtrack=[0 for _ in range(r)]
        ctrack = [0 for _ in range(c)]

        for i in range (0,r):
            for j in range (0,c):
                if matrix [i][j]==0:
                    rtrack [i] = -1
                    ctrack [j] =-1

        for i in range (0,r):
            for j in range(0,c):
                if rtrack[i]== -1 or ctrack[j]==-1:
                    matrix[i][j]=0                     