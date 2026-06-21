class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def check(rate):
            hours = 0
            for pile in piles:
                hours += -(-pile // rate)   # ceil(pile/rate)
            return hours

        ans = right

        while left <= right:
            mid = (left + right) // 2

            if check(mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans