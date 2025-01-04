from collections import defaultdict


def myJoin(inside: list[str], rightof: list[str]) -> list[str]:
    """
    Computes all possible string combinations of the form `(inside)rightof`

    Parameters
    ----------
    inside : list[str]
        all allowable strings that can go inside the group on the left
    rightof : list[str]
        all allowable strings that can go to the right of the first group

    Returns
    -------
    res : list[str]
        all possible combinations
    """
    res = []
    for x in inside:
        left = "(" + x + ")"
        for y in rightof:
            res.append(left + y)
    return res


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Notes
        -----
        - Obviously we have to start with an open parentheses
        - Let's say we open parentheses #1 (0-indexed)
            - We have to close them eventually, but we can close after
              0 additional pairs, 1 additional pairs... `n-1` additional pairs
            - We split the string into `(INSIDE)RIGHTOF` where the number of pairs
              in `pairs(inside) + pairs(rightof) = n-1` since we have the pair enclosing
              `inside`
            - We start with `n=2` and work our way up, generating all pairs of all
              `inside` and `rightof` strings
            - Let's say we choose to close with `k` additional pairs inside,
              then we have `generateParenthesis(k)` + `generateParentheses(n-k-1)`
              ways
        """
        # create results and initialize the first few values
        res = defaultdict(list)
        res[0] = [""]
        res[1] = ["()"]
        res[2] = ["(())", "()()"]

        # DP
        for i in range(3, n + 1):  # total # of pairs in the string
            for k in range(i):  # number of pairs inside the "first" grouping, [0, i-1]
                # ways to arrange the `k` pairs inside the first grouping
                L1 = res[k]

                # ways to arrange the `i-k-1` pairs to the right
                L2 = res[i - k - 1]

                # combine (this is SLOW)
                res[i] += myJoin(L1, L2)
        return res[n]
