from heapq import heappop, heappush


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        """
        Computes the maximum average pass ratio of the classes given the current number of
        passing and total students for each class, and given a pile of "brilliant" students
        who can be added to any class and are guaranteed to pass.

        Notes
        -----
        - At each step, we can add 1 student. How can we add the student to have the largest impact on the average?
        - Basically we want to find argmax over `i` of `(pi+1)/(ti+1) - pi/ni = (ti-pi)/(ti^2+ti)`
          since that tells us which class' average will increase the most with the addition of a single passing student

        Parameters
        ----------
        classes : list[list[int]]
            tuples of `(pass_i, total_i)` for each class
        extraStudents : int
            number of "brilliant" students available

        Returns
        -------
        avg : float
            best average pass ratio
        """

        # We're going to use a max heap of tuples (V, i)
        #   where `V = (total_i - pass_i)/(total_i^2 + total_i)`
        # This is derived from `V = (pass_i+1)/(total_i+1) - pass_i/total_i`
        # meaning `V` is the change in the pass ratio if we add a passing student
        maxheap = []
        for i, (pi, ti) in enumerate(classes):
            vi = (ti - pi) / (ti * ti + ti)
            heappush(maxheap, (-vi, i))

        # for each student, pop off the heap, update the pass and total for that
        # class, push updated value onto the heap
        for k in range(extraStudents):
            # pop from stack
            _, idx = heappop(maxheap)

            # update pass and total for this class
            classes[idx][0] += 1
            classes[idx][1] += 1

            # compute new `V` and push to heap
            pi, ti = classes[idx]
            vi = (ti - pi) / (ti * ti + ti)
            heappush(maxheap, (-vi, idx))

        # compute average
        S = sum([pi / ti for pi, ti in classes]) / len(classes)
        return S


# Topics: Heap, Greedy
