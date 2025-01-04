class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Notes
        -----
        - The technique is to satisfy the least-greedy kid with the smallest
          possible cookie at each time
        """
        # sort the two
        g.sort()
        s.sort()

        cnt = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1  # increase the count of satisfied kids
                i += 1  # move to the next child
            j += 1
        return cnt
