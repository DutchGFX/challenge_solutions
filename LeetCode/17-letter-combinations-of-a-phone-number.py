from itertools import product

mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
mapping = {key: [c for c in val] for key, val in mapping.items()}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        tmp = [mapping[d] for d in digits]
        combs = product(*tmp)
        return ["".join(c) for c in combs]
