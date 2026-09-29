class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Arrange cars as position:speed pairs
        cars = [(position[i], speed[i]) for i in range(len(position))]
        # Sort the cars by position
        cars.sort()
        # Initialize array for actual arrival times
        arrival_times = [0] * len(position)
        # For each car starting with the frontmost,
        for i in reversed(range(len(cars))):
            # Calculate expected arrival time
            expected_arrival = (target - cars[i][0]) / cars[i][1]
            # Store real arrival time as the later of expected arrival and actual arrival of car in front of you
            arrival_times[i] = max(expected_arrival, arrival_times[i + 1]) if i + 1 < len(cars) else expected_arrival
        # Return the number of distinct arrival times
        return len(set(arrival_times))
