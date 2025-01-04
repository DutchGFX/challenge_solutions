from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        # hashmaps store first occurence in either direction
        # chars_left stores the index of the FIRST occurence going left to right
        chars_l2r, chars_r2l = {}, {}
        for i in range(len(s)):
            # if an index occurs later, it will be overwritten,
            # hence this gives the first index going right to left
            chars_r2l[s[i]] = i

            # if the charatcer occurs earlier, we will overwrite the index,
            # hence this gives the first occurence going left to right
            chars_l2r[s[-1 - i]] = len(s) - i - 1

        # valid "bracketing" characters
        chars = {chr(i): [-1, -1] for i in range(ord("a"), ord("z") + 1)}
        chars.update({c: (a, chars_r2l[c]) for c, a in chars_l2r.items() if chars_r2l[c] - a > 1})

        # loop
        results = set()
        brackets = set()
        for i, c in enumerate(s):
            # if this is the end of the bracket for this character, remove
            if chars[c][1] == i:
                brackets.remove(c)

            # loop over brackets
            results |= {b + c + b for b in brackets}

            # add this as the start of a new bracket
            if chars[c][0] == i:
                brackets.add(c)

        return len(results)
