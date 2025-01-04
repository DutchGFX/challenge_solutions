class Solution:
    def maxScore(self, s: str) -> int:
        # total number of zeros
        num_zeros = s.count("0")

        # loop
        left, m = 0, 0
        for i in range(len(s) - 1):
            # number of zeros up to and including s[i]
            left += s[i] == "0"

            # we can figure out how many zeros remain using the total number of zeros
            #   `rem = num_zeros - left`
            # we can then figure out how many ones are on the right because we have `len(s) - i - 1`
            # characters on the right
            right = (len(s) - i - 1) - (num_zeros - left)
            m = max(m, left + right)
        return m
