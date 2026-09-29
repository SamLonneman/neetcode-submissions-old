class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Arrange cars as position:speed pairs
        cars = list(zip(position, speed))
        # Sort the cars by position
        cars.sort()
        # Initialize a stack to hold increasing arrival times of each fleet
        fleet_arrival_times = []
        # For each car starting with the frontmost,
        for i in reversed(range(len(cars))):
            # Calculate expected arrival time
            expected_arrival = (target - cars[i][0]) / cars[i][1]
            # If arriving later than the latest fleet, start a new fleet
            if not fleet_arrival_times or expected_arrival > fleet_arrival_times[-1]:
                fleet_arrival_times.append(expected_arrival)
        # Return the number of fleets
        return len(fleet_arrival_times)
