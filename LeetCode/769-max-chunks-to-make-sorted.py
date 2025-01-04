from heapq import heapify, heappop, heappush


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """
        Computes the maximum number of chunks into which we can divide an array for chunk-wise sorting

        Parameters
        ----------
        arr : list[int]
            numbers

        Returns
        -------
        num_splits : int
            number of times we can split the array

        Notes
        -----
        - All the values to the left of a split must be less than all the values to the right of the split
        - If at any point, the `n` smallest values are all to the left of index `n`, then we can split the array
          at index `n`
            - The `n` smallest values can be sorted, and then the remaining values can be sorted
        - We use a minheap to pop the smallest values from the array
        - If we pop an item from the stack and it is to the right of the proposed split, we know we can't split there,
          as there must be at least one value in the middle, currently unfilled, that is farther to the right
        - We increment the count of "smallest elements" that we pop from the stack
        - If that count is equal to the proposed split index, we can split the array at that point
        """

        # create the minheap
        H = [(x, idx) for idx, x in enumerate(arr)]
        heapify(H)

        # what if we keep popping until we have a full "set" of 0:N on the right
        num_splits = 0  # number of times we split
        cnt = 0  # count of smallest elements popped off the stack so far
        split_ind = 0  # index at which we propose a split
        while H:  # while items in heap
            # pop from the heap
            num, idx = heappop(H)

            # update split index since we know that all values to the right must be larger if we are
            # going to split at this index
            split_ind = max(split_ind, idx)
            cnt += 1

            # if we are splitting, we must have every element to the left
            if cnt == split_ind + 1:
                num_splits += 1

        return num_splits
