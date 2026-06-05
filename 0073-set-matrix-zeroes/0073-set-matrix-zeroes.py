class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # boolean variable for indicating that zeroth row should be zero
        zeroRow = False

        # go through the matrix and check 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # mark that this col needs to be updated to zero
                    matrix[0][c] = 0

                    # mark that this row needs to be zero
                    if r > 0:       # if r is not 0
                        matrix[r][0] = 0
                    else:
                        zeroRow = True

        # update based on what we found
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if zeroRow:
            for c in range(COLS):
                matrix[0][c] = 0