def update_dictionary():
    pass


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Notes
        -----
        - Substring === contiguous characters
        - We want the longest substring that contains `k` "mismatched" characters
        - We use a dictionary to store the counts
        """

        # d stores the character counts
        d = {}

        max_cnt = 0
        L_max = 0
        right = 0
        left = 0
        for right in range(len(s)):
            # increment count for current character
            d[s[right]] = d.get(s[right], 0) + 1

            # check if new max
            max_cnt = max(d[s[right]], max_cnt)

            # if we need to shrink the interval,
            # we need to shrink it by 1 character
            # at most, since we only added one character
            # now, we actually don't care about "reducing"
            # `max_cnt` at all, because if we reduce `max_cnt`,
            # we would need to flip more numbers, so we are just
            # looking for the largest `max_cnt`
            if (right - left + 1) - max_cnt > k:
                d[s[left]] -= 1
                left += 1
                continue

            # update max window size
            L_max = max(L_max, right - left + 1)

        return L_max
