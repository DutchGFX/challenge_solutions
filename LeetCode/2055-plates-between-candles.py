def init_arrays(s: str):
    """
    TODO:
    """
    # compute arrays that store the index of the next and previous candle
    # also compute an array of the number of plates
    next_candle = [(len(s) - 1) if s[-1] == "|" else None] * len(s)
    prev_candle = [0 if s[0] == "|" else None] * len(s)
    num_plates = [1 * (s[0] == "*")] * len(s)

    for i in range(1, len(s)):
        # moving left to right to find the "prev" candle
        isCandle = s[i] == "|"
        num_plates[i] = num_plates[i - 1] + (not isCandle)
        prev_candle[i] = i if isCandle else prev_candle[i - 1]

        # moving left to right to find the "next" candle
        k = len(s) - 1 - i
        isCandle = s[k] == "|"
        next_candle[k] = k if isCandle else next_candle[k + 1]

    return num_plates, next_candle, prev_candle


class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        """

        Notes
        -----
        - We are going to store the cumulative sum of the candles
        - For each query, we need to find the first and last candle, then return
          the number of plates between those two indices
        - This might not be the *most* efficient way, but it's efficient enough, I think,
          though if we consider the case where there are a lot of plates on both sides of the
          substring, we might run into problems
        - what if we make arrays that store the next plate to the right and left of each index?
        """

        # initialize results
        res = [0] * len(queries)

        # edge case
        if not s:
            return res

        num_plates, next_candle, prev_candle = init_arrays(s)

        # loop over the queries
        for idx, (i, j) in enumerate(queries):
            # get indices of the first and last candle in this string
            left = next_candle[i]  # first candle
            right = prev_candle[j]  # last candle

            # if there aren't two candles in the string, res=0
            if (left is None) or (right is None) or (left >= right):
                continue

            res[idx] = num_plates[right] - num_plates[left]

        return res


# Topics: Prefix Sum
