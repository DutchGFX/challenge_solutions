class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The sum of a subarray from `[i,j]` is `prefix[j] - prefix[i]`.
        # We want to maximize this. For any `j`, we want to use the smallest
        # `prefix[i]` so far
        maxsum = -float("inf")
        minprefix = 0
        prefix = 0
        for n in nums:
            # update prefix sum
            prefix += n

            # see if we have a new max
            maxsum = max(maxsum, prefix - minprefix)

            # update the smallest prefix sum
            minprefix = min(minprefix, prefix)
        return maxsum
