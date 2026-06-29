import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        heap = []

        for num in arr:
            dist = abs(num - x)

            heapq.heappush(heap, (-dist, -num))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        while heap:
            ans.append(-heapq.heappop(heap)[1])

        return sorted(ans)