class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # extend heaters to make intervals to bracket the houses
        heaters = [-float("inf")] + heaters + [float("inf")]

        # sort
        heaters.sort()
        houses.sort()

        maxmin_dist = -1e14
        j = 0  # heaters[i] < houses[j] <= heaters[i+1]
        for i in range(len(heaters) - 1):
            while (j < len(houses)) and (houses[j] <= heaters[i + 1]):
                min_dist = min(houses[j] - heaters[i], heaters[i + 1] - houses[j])
                maxmin_dist = max(maxmin_dist, min_dist)
                j += 1
        return maxmin_dist
