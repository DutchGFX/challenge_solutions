class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        Computes the minimum number of intervals we need to delete
        to end up with non-overlapping intervals. Note that intervals do
        not include their boundary times, so and interval that starts at T
        does not overlap with an interval ending at T

        Parameters
        ----------
        interval : list[list[int]]
            list of (start_time, end_time) of intervals

        Returns
        -------
        cnt : int
            minimum number of intervals to delete

        Notes
        -----
        We know that for every interval, we either:
        (a) keep the interval, or
        (b) delete all intervals overlapping it

        So what we do is we start with an interval and then while things overlap, we consistently
        delete the interval with the later end time, since that will overlap the most intervals
        in the future
        """

        # sort the intervals by start time
        intervals.sort()

        # loop
        cnt = 0
        left = 0  # current left interval
        right = 1  # current right interval
        while right < len(intervals):
            right = max(right, left + 1)

            # if the next interval doesn't overlap, skip to next interval
            if intervals[right][0] >= intervals[left][1]:
                left = right
                right = left + 1
                continue

            # if we get here, they overlap, so we delete the interval that starts later
            cnt += 1
            if intervals[left][1] > intervals[right][1]:  # delete the left interval
                left = right

            right += 1

        return cnt


# Topics: Intervals, Greedy
