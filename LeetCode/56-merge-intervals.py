class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Notes
        -----
        - We sort by the start of the intervals
        """
        # sort by start
        intervals.sort()

        # initialize output
        output = [intervals[0]]

        for start, end in intervals:
            # if overlapping, see if we need to expand
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:  # if not overlapping, append new interval
                output.append([start, end])
        return output
