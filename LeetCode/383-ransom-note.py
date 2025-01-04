from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Uses counters
        """
        C_rn = Counter(ransomNote)
        C_m = Counter(magazine)

        # loop and check each character count
        for char_in_rn, cnt_in_rn in C_rn.items():
            if C_m.get(char_in_rn, 0) < cnt_in_rn:
                return False
        return True
