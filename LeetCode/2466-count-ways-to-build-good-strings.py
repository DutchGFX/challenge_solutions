class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        At each step, we can do one of the following:
            - Append the character `'0'` `zero` times
            - Append the character `'1'` `one` times
        The final string must have a length between `low` and `high` (inclusive)
        Return the

        Returns
        -------
        res : int
            number of ways to construct the string, modulo `10^9 + 7`


        Notes
        -----
        - Obviously if the length `N < min(zero, one)`, we can't construct the string,
          so that's the lower limit on the dynamic programming approach.
        - We ADD the DP results at each step to avoid overwriting the placeholder
          for the `one` and `zero`
        - We sum the results from `low` to `high`
        """
        # will hold the total count
        res = 0

        # initialize DP
        # `DP[i]` is the number of ways to create a string of size `i`
        DP = [0] * (high + 1)
        DP[zero] += 1
        DP[one] += 1  # we will u
        for i in range(min(one, zero), high + 1):
            DP[i] += DP[i - zero] + DP[i - one]
            if i >= low:
                res += DP[i]

        return res % (10**9 + 7)
