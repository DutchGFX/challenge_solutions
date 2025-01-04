class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Notes
        -----
        - Update to `None` if we need to set to `0`. This lets us avoid duplicates/chaining
        - We then go back and update the `None` to `0`
        """
        # extract sizes
        M, N = len(matrix), len(matrix[0])

        # nested FOR loops
        # set to NONE if we need to set it to 0 later
        for i in range(M):
            for j in range(N):
                # skip if already visited (None) or not 0
                if matrix[i][j] != 0:
                    continue

                # zero elements in column
                for r in range(M):
                    if matrix[r][j] != 0:
                        matrix[r][j] = None
                for c in range(N):
                    if matrix[i][c] != 0:
                        matrix[i][c] = None

        # update None to `0`
        for i in range(M):
            for j in range(N):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
