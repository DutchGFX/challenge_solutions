class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        Maximizes the sightseeing value, given by
        `values[i] + values[j] + i - j` where `i<j`

        Parameters
        ----------
        values : list[int]
            list of sightseeing values

        Returns
        -------
        maxval : int
            maximum sightseeing value

        Notes
        -----
        - WLOG, require `i<j`
        - We want to, independently, maximize `values[i] + i` up to `j`
        - We loop over `j`, and we store the "best" `i` up until that `j`
        """

        maxval_i = -1e14
        maxval = -1e14
        for j in range(1, len(values)):
            # update the "best" i
            maxval_i = max(maxval_i, values[j - 1] + j - 1)

            # update the best overall answer
            maxval = max(maxval, maxval_i + values[j] - j)

        return maxval
