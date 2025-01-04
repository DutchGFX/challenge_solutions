class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Parameters
        ----------
        nums : list[int]
            step sizes

        Returns
        -------
        can_reach : bool
            True if we can reach the top step from step 0

        Notes
        -----
        - Each number is the MAXIMUM jump at each step
        - We want to work backwards, storing the smallest index from which
          we can reach the top
        - At each step, we check if we can reach that index. If we can,
          this step becomes the new smallest index
        """
        # we know we can reach the last index index from the last index itself
        min_index = len(nums) - 1

        # go in reverse order
        for i in range(len(nums) - 1, -1, -1):
            min_index = i if (i + nums[i] >= min_index) else min_index

        return min_index == 0
