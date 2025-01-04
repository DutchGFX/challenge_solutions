class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Comutes the final price of items in a shop using a
        "special" discount

        Parameters
        ----------
        prices : list[int]
            item prices

        Returns
        -------
        res : list[int]
            final prices
        """
        # copy prices to results, assuming no discount
        res = [p for p in prices]

        S = []  # stack
        for j, p in enumerate(prices):
            # while p[j] <= p[i], pop the items in the queue off the stack
            # since we want to find the first index that satisfies the requirement.
            # Once we find it, we don't need to look for index `i` anymore
            while S and S[-1][0] >= p:
                _, i = S.pop(-1)
                res[i] -= p

            # push onto stack
            S.append((p, j))

        return res
