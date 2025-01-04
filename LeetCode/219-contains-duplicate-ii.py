class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # we will store the most recent instance of each number
        most_recent = {}
        for i, num in enumerate(nums):
            if num in most_recent and abs(i - most_recent[num]) <= k:
                return True
            most_recent[num] = i
        return False
