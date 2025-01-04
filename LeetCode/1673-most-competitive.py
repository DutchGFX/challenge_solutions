class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        # initialize empty stack
        S = []

        # for each number
        N = len(nums)
        for i in range(N):
            # while smaller AND we have enough remaining numbers to hit `k`
            rem = N - i - 1  # number of remaining numbers
            while S and (rem + len(S) >= k) and nums[i] < S[-1]:
                S.pop(-1)
            S.append(nums[i])
        return S[:k]
