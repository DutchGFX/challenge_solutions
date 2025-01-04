class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to
        get to the top of the staircase when we
        can climb either 1 or 2 steps at each instance

        Parameters
        ----------
        n : int
            number of steps

        Notes
        -----
        - We can reach level `i` from either level `i-1` or level `i-1`
        """
        # there is 1 way to reach level 0
        # there is also 1 way to reach level 1
        DP = [1] * (n + 1)

        # dynamic programming
        for i in range(2, n + 1):
            DP[i] = DP[i - 1] + DP[i - 2]
        return DP[-1]
