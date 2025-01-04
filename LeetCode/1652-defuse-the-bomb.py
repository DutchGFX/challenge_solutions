class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0:  # edge case
            return [0] * len(code)
        elif k < 0:  # reverse list, invert k, recurse
            return self.decrypt(code[::-1], -k)[::-1]

        # now we only have to deal with the positive case
        # we will use a running sum so we only have to do 1 addition and 1 subtraction for each element
        decoded = [0] * len(code)
        decoded[0] = sum(code[1 : 1 + k])  # initialize the first sum
        for i in range(1, len(code)):  # for other entries
            j = (i + k) % len(code)
            decoded[i] = decoded[i - 1] + code[j] - code[i]
        return decoded
