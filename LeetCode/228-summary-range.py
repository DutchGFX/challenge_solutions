class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # edge case
        if len(nums) == 0:
            return []

        res = []
        start = nums[0]
        nums.append(float("inf"))  # helps with the loop logic
        for i in range(1, len(nums)):
            # if in the same interval, continue
            if (d := nums[i] - nums[i - 1]) == 1:
                continue

            # break interval
            if nums[i - 1] == start:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{nums[i-1]}")

            # update for next interval
            start = nums[i]
        return res
