class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
     

        fleet_count = 0
        time = []

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            time.append((position[i], t))

        time.sort(reverse=True)

        fleet_time = 0

        for i in range(len(time)):
            current_time = time[i][1]

            if current_time > fleet_time:
                fleet_count += 1
                fleet_time = current_time

        return fleet_count