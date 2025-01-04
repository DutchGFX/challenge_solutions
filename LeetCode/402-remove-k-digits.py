class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Notes
        -----
        - Priority #1 is getting the smallest possible leading digit
        - I think that's the idea, and we can call the function recursively after that
        - Use a stack to keep track, count deletions along the way
            - Delete if number is smaller
        """

        # edge case
        if len(num) <= k:
            return "0"

        L = []  # cumulative list of characters
        cnt = 0  # number of deleted characters
        for x in num + "0" * k:  # for each character
            while L and (x < L[-1]) and (cnt < k):
                cnt += 1
                L.pop(-1)
            L.append(x)
        s = "".join(L[:-k]).lstrip("0")
        if not s:
            return "0"
        return s
