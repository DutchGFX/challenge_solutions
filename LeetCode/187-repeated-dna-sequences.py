class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seqs = set()  # sequences that appear at all
        seqs_repeated = set()  # initialize sequencies
        for i in range(len(s) - 9):
            tmp = s[i : i + 10]  # extract sequence
            if tmp in seqs:  # if we already have this sequence
                seqs_repeated.add(tmp)  # append to list
            seqs.add(tmp)  # add to the set
        return list(seqs_repeated)
