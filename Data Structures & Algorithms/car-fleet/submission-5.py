class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        cars = sorted(zip(position, speed), reverse=True)

        fleet = len(cars)

        min_time = (target - cars[0][0]) / cars[0][1]

        for p, s in cars[1:]:
            time = (target - p) / s

            if time <= min_time:
                fleet -= 1
            else:
                min_time = time

        return fleet