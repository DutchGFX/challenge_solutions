class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # start with the least significant digit
        i = len(digits) - 1  # index to add to
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i >= 0:
            digits[i] += 1
        else:
            digits = [1] + digits
        return digits
