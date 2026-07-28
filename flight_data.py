from flight import Flight

class FlightData:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def show_all_flights(self):
        for flight in self.flights:
            print(flight)