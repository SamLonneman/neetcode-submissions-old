class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        arrival_times = [0] * len(position)
        for i in range(len(cars)):
            expected_arrival = (target - cars[i][0]) / cars[i][1]
            arrival_times[i] = max(expected_arrival, arrival_times[i - 1]) if i > 0 else expected_arrival
        return len(set(arrival_times))
