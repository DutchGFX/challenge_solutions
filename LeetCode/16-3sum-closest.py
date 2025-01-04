class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        Finds the 3 integers that sum to a value closest to the target value

        Parameters
        ----------
        nums : list[int]
            numbers to sum
        target : int
            desired sum

        Returns
        -------
        S : int
            sum of the integers closest to target

        Notes
        -----
        Assume WLOG that i<j<k.
        Starting from `a=nums[i]``, and `b=nums[i+1]`, the largest sum is created using the last index.
        We then decrement the last index until we are smaller than the target. We then incremement `j`
        until we are once again larger than the target, then we decrement `k`, and on and on...
        """
        # sort
        nums.sort()
        mindiff = 1e14
        closest = None

        # for each i, we start at j=i+1 and find the point at
        # which we cross from >target to sum<target.
        # then we increment j and move k in the opposite direction,
        # and then we repeat. Then we increase i and repeat
        for i, a in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                S = a + nums[j] + nums[k]

                # update closest
                if (d := abs(S - target)) < mindiff:
                    closest = S
                    mindiff = d

                # if larger than target, decrement k to get a smaller sum
                # if smaller than target, increase j to get a larger sum
                if S > target:
                    k -= 1
                else:
                    j += 1

        return closest
