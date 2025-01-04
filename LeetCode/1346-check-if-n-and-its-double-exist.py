class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        d = {}
        for x in arr:
            if (2 * x in d) or (x / 2 in d):
                return True
            d[x] = 1
        return False
