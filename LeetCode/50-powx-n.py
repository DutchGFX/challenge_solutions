class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Computes `x^n` by computing `x^(n//2)` and squaring
        the result. Does this recursively
        """
        # if negative, recurse
        if n < 0:
            return 1 / self.myPow(x, abs(n))

        if n == 0:
            return 1.0

        # we should do n//2 twice,
        v2 = self.myPow(x, n // 2)
        v = v2 * v2
        if n % 2 == 1:
            v *= x
        return v
