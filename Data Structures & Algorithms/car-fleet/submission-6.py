class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=len(position)
        cars=[]
        if not position:
            return 0

        for i in range(len(position)):
            cars.append((position[i],speed[i]))

        cars.sort(reverse=True)
        
        min_time=(target-cars[0][0])/cars[0][1]

        for p,s in cars[1:]:
            time=(target-p)/s
            if time<=min_time:
                fleet-=1
            else:
                min_time=time

        return fleet



        