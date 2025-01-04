class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        """
        Finds the unique champion of the Directed Acyclic Graph (DAG).
        If there is no unique champion, returns -1

        Notes
        -----
        - We want to find all the nodes that do not have any other node that leads to them.
        - This is the same as finding all nodes that are not in the set of edge endpoints.
        - We compute the set of edge endpoints, then find the champion
        """
        # set of all edge endpoints
        # these are all the nodes that have a "stronger" team
        s = set([weaker for stronger, weaker in edges])

        # if there aren't `N-1` teams with no stronger team,
        # we don't have a unique champion, so return -1
        if len(s) != n - 1:
            return -1

        # find the champion
        for i in range(n):
            if i not in s:
                return i
