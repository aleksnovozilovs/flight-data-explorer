class Flight:
    def __init__(self, flight_number, airline, origin, destination, altitude):
        self.flight_number = flight_number
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.altitude = altitude 

    def __str__(self):
        return (
            f"{self.flight_number} | {self.airline} | "
            f"{self.origin} -> {self.destination} |"
            f"{self.altitude} ft"   
        )