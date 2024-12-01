class Vehicle:
    def __init__(self, mode, speed_kmh, cost_per_km, transfer_time_min):
        self.mode = mode
        self.speed_kmh = speed_kmh
        self.cost_per_km = cost_per_km
        self.transfer_time_min = transfer_time_min

    def calculate_time(self, distance_km):
        """
        Calculate travel time for the given distance in minutes.
        """
        return (distance_km / self.speed_kmh) * 60 + self.transfer_time_min

    def calculate_cost(self, distance_km):
        """
        Calculate travel cost for the given distance in won.
        """
        return distance_km * self.cost_per_km