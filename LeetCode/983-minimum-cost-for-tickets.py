class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Notes
        -----
        - At each step, if we need a ticket that day, we can either:
            - buy a 1 day pass
            - have bought a 7-day pass less than 7 days prior
            - have bought a 30-day pass less than 30 days prior
        - If we bought a prior pass, we can "jump" those middle days
          since we won't incur any additional costs, since the ticket
          will cover those days
        - As a result, we can take the minimum over 1,7,30 of the cost `X` days prior,
          plus the cost of an `X`-day pass purchased `X-1` days ago

        """
        # convert to hashmap for easy checking
        days = set(days)

        # DP[i] stores the minimum cost so far
        DP = [0] * 366

        # for each day. We use 0 to make the recursion cleaner
        for i in range(1, 366):
            # if not a travel day, we don't need to buy a pass
            if i not in days:
                DP[i] = DP[i - 1]
                continue

            # compute minimum cost of buying the various passes

            # First, we could buy a day pass, so let that be the default
            DP[i] = DP[i - 1] + costs[0]

            # We could have bought a 7-day pass 6 days ago,
            # in which case our cost would be the minimum cost 7 days ago,
            # plus the cost of the 7-day pass
            DP[i] = min(DP[i], DP[max(0, i - 7)] + costs[1])

            # We could have bought a 30-day pass 29 days ago
            DP[i] = min(DP[i], DP[max(0, i - 30)] + costs[2])

        return DP[-1]
