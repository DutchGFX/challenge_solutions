class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        cnt = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if (s := nums[i] + nums[j]) > k:
                j -= 1
            elif s == k:
                cnt += 1
                i += 1
                j -= 1
            else:
                i += 1
        return cnt
