class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Notes
        -----
        - We basically need to count how many times in a row we increase in either direction
        - Bascially the number of candies is the number of stairs we had to climb in one direction
        - We initialize to 1, and then we simultaneously go left to right and right to left,
          taking the maximum "height" of the position to mean the number of "stairs" we had to climb
          in either direction, since that's the minimum number of candies we need
        - For example, if we have ratings in a row that increase, the 5th person must have at least 5 candies
        """
        # array approach, first attempt
        candies = [1] * len(ratings)

        # go right to left
        for i in range(1, len(ratings)):
            # right to left. If we had to go up a tier
            if ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], 1 + candies[i - 1])

            # left to right
            k = -1 - i
            if ratings[k] > ratings[k + 1]:
                candies[k] = max(candies[k], 1 + candies[k + 1])
        return sum(candies)
